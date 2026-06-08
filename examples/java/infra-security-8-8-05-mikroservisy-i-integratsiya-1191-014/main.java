// src/main/java/ru/timur/crm/CrmController.java
package ru.timur.crm;

import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import org.apache.kafka.clients.admin.AdminClient;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.producer.RecordMetadata;
import ru.timur.crm.config.DatabaseConfig;
import ru.timur.crm.config.KafkaConfig;
import ru.timur.crm.model.Customer;
import ru.timur.crm.producer.CustomerProducer;
import ru.timur.crm.service.CustomerService;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.time.Duration;
import java.util.Collections;
import java.util.Properties;
import java.util.UUID;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class CrmController {
    @FXML private Label kafkaStatus;
    @FXML private Label dbStatus;
    @FXML private TextField idField;
    @FXML private TextField nameField;
    @FXML private TextField emailField;
    @FXML private TextField phoneField;
    @FXML private Label partitionsInfo;
    @FXML private Label totalMessages;
    @FXML private TextArea logArea;

    private AdminClient adminClient;
    private CustomerProducer customerProducer;
    private Connection dbConnection;
    private ExecutorService executor = Executors.newCachedThreadPool();

    // Потребитель Kafka
    private KafkaConsumer<String, Customer> kafkaConsumer;
    private ExecutorService consumerExecutor;
    private volatile boolean isConsumerRunning = false;

    @FXML
    public void initialize() {
        generateId();
        nameField.setText("Тестовый клиент");
        emailField.setText("test@example.com");
        phoneField.setText("+79001234567");
    }

    @FXML
    public void connectToKafka() {
        try {
            Properties adminProps = new Properties();
            adminProps.put("bootstrap.servers", "localhost:9092");
            this.adminClient = AdminClient.create(adminProps);
            adminClient.listTopics().names().get();
            this.customerProducer = new CustomerProducer();

            Platform.runLater(() -> {
                kafkaStatus.setText("Подключено");
                kafkaStatus.setStyle("-fx-text-fill: green;");
            });
            log("Успешное подключение к Kafka");
            updateTopicInfo();

        } catch (Exception e) {
            Platform.runLater(() -> {
                kafkaStatus.setText("Ошибка подключения");
                kafkaStatus.setStyle("-fx-text-fill: red;");
            });
            log("Ошибка подключения к Kafka: " + e.getMessage());
        }
    }

    @FXML
    public void connectToDb() {
        try {
            this.dbConnection = DriverManager.getConnection(
                    DatabaseConfig.DB_URL,
                    DatabaseConfig.DB_USER,
                    DatabaseConfig.DB_PASSWORD
            );

            Platform.runLater(() -> {
                dbStatus.setText("Подключено");
                dbStatus.setStyle("-fx-text-fill: green;");
            });
            log("Успешное подключение к PostgreSQL");

        } catch (Exception e) {
            Platform.runLater(() -> {
                dbStatus.setText("Ошибка подключения");
                dbStatus.setStyle("-fx-text-fill: red;");
            });
            log("Ошибка подключения к БД: " + e.getMessage());
        }
    }

    @FXML
    public void sendToKafka() {
        if (customerProducer == null) {
            log("Ошибка: не подключено к Kafka");
            return;
        }

        executor.submit(() -> {
            try {
                Customer customer = new Customer(
                        idField.getText(),
                        nameField.getText(),
                        emailField.getText(),
                        phoneField.getText()
                );

                var future = customerProducer.sendCustomerCreated(customer);
                RecordMetadata metadata = future.get();

                Platform.runLater(() -> {
                    log(String.format("✓ Отправлено: ID=%s, партиция=%d, смещение=%d",
                            customer.getId(), metadata.partition(), metadata.offset()));
                    updateTopicInfo();
                    generateId();
                    nameField.clear();
                    emailField.clear();
                    phoneField.clear();
                });

            } catch (Exception e) {
                Platform.runLater(() ->
                        log("✗ Ошибка отправки в Kafka: " + e.getMessage())
                );
            }
        });
    }

    @FXML
    public void startConsumer() {
        if (isConsumerRunning) {
            log("⚠ Потребитель уже запущен");
            return;
        }

        if (dbConnection == null) {
            log("✗ Ошибка: подключитесь к БД перед запуском потребителя");
            return;
        }

        try {
            Properties props = new Properties();
            props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
            props.put(ConsumerConfig.GROUP_ID_CONFIG, "crm-gui-consumer");
            props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG,
                    "org.apache.kafka.common.serialization.StringDeserializer");
            props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG,
                    "ru.timur.crm.serializer.JsonDeserializer");
            props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
            props.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, "false");

            this.kafkaConsumer = new KafkaConsumer<>(props);
            kafkaConsumer.subscribe(Collections.singletonList(KafkaConfig.CUSTOMER_TOPIC));

            this.consumerExecutor = Executors.newSingleThreadExecutor();
            this.isConsumerRunning = true;

            consumerExecutor.submit(() -> {
                log("✓ Потребитель запущен, слушает топик: " + KafkaConfig.CUSTOMER_TOPIC);

                while (isConsumerRunning) {
                    try {
                        ConsumerRecords<String, Customer> records =
                                kafkaConsumer.poll(Duration.ofMillis(500));

                        if (records.count() > 0) {
                            for (var record : records) {
                                Customer customer = record.value();

                                try (CustomerService service = new CustomerService(dbConnection)) {
                                    service.saveCustomer(customer);
                                    kafkaConsumer.commitSync();

                                    Platform.runLater(() -> {
                                        log(String.format("✓ Получен клиент из Kafka: ID=%s, Имя=%s",
                                                customer.getId(), customer.getName()));
                                    });
                                } catch (SQLException e) {
                                    Platform.runLater(() ->
                                            log("✗ Ошибка сохранения в БД: " + e.getMessage())
                                    );
                                }
                            }
                        }
                    } catch (Exception e) {
                        if (isConsumerRunning) {
                            Platform.runLater(() ->
                                    log("⚠ Ошибка потребителя: " + e.getMessage())
                            );
                            try { Thread.sleep(1000); } catch (InterruptedException ie) { Thread.currentThread().interrupt(); }
                        }
                    }
                }

                try {
                    kafkaConsumer.close();
                } catch (Exception e) {
                    Platform.runLater(() ->
                            log("⚠ Ошибка при закрытии потребителя: " + e.getMessage())
                    );
                }

                Platform.runLater(() ->
                        log("✓ Потребитель остановлен")
                );
            });

        } catch (Exception e) {
            log("✗ Ошибка запуска потребителя: " + e.getMessage());
            isConsumerRunning = false;
        }
    }

    @FXML
    public void stopConsumer() {
        if (!isConsumerRunning) {
            log("⚠ Потребитель не запущен");
            return;
        }

        isConsumerRunning = false;
        if (consumerExecutor != null) {
            consumerExecutor.shutdownNow();
        }
    }

    @FXML
    public void generateId() {
        idField.setText(UUID.randomUUID().toString());
    }

    @FXML
    public void loadCustomersFromDb() {
        if (dbConnection == null) {
            log("Ошибка: не подключено к БД");
            return;
        }

        executor.submit(() -> {
            try {
                Statement stmt = dbConnection.createStatement();
                ResultSet rs = stmt.executeQuery("SELECT * FROM customers ORDER BY created_at DESC LIMIT 10");

                StringBuilder sb = new StringBuilder("Последние клиенты из БД:\n");
                int count = 0;
                while (rs.next()) {
                    count++;
                    sb.append(String.format("  %d. ID: %s\n     Имя: %s, Email: %s, Телефон: %s\n",
                            count,
                            rs.getString("id"),
                            rs.getString("name"),
                            rs.getString("email"),
                            rs.getString("phone")));
                }
                if (count == 0) sb.append("  Нет клиентов в базе данных");

                Platform.runLater(() -> log(sb.toString()));

            } catch (Exception e) {
                Platform.runLater(() ->
                        log("✗ Ошибка загрузки из БД: " + e.getMessage())
                );
            }
        });
    }

    @FXML
    public void clearLog() {
        logArea.clear();
    }

    private void updateTopicInfo() {
        if (adminClient == null) return;

        executor.submit(() -> {
            try {
                var topicResult = adminClient.describeTopics(Collections.singletonList(KafkaConfig.CUSTOMER_TOPIC));
                var description = topicResult.values().get(KafkaConfig.CUSTOMER_TOPIC).get();
                int partitionCount = description.partitions().size();

                Platform.runLater(() -> {
                    partitionsInfo.setText(String.valueOf(partitionCount));
                    totalMessages.setText("--");
                });

            } catch (Exception e) {
                Platform.runLater(() -> {
                    partitionsInfo.setText("Ошибка");
                    totalMessages.setText("Ошибка");
                });
            }
        });
    }

    private void log(String message) {
        Platform.runLater(() -> {
            logArea.appendText("[" + java.time.LocalTime.now().toString().substring(0, 8) + "] " + message + "\n");
            logArea.setScrollTop(Double.MAX_VALUE);
        });
    }

    public void shutdown() {
        stopConsumer();
        if (customerProducer != null) {
            customerProducer.close();
        }
        if (dbConnection != null) {
            try { dbConnection.close(); } catch (Exception e) { /* ignore */ }
        }
        if (adminClient != null) {
            adminClient.close();
        }
    }
}
