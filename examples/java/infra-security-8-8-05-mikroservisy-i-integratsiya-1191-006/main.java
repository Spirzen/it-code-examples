// src/main/java/ru/timur/crm/consumer/CustomerConsumer.java
package ru.timur.crm.consumer;

import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import ru.timur.crm.config.KafkaConfig;
import ru.timur.crm.model.Customer;
import ru.timur.crm.service.CustomerService;

import java.sql.SQLException;
import java.time.Duration;
import java.util.Collections;

public class CustomerConsumer implements Runnable {
    private final KafkaConsumer<String, Customer> consumer;
    private final CustomerService customerService;

    public CustomerConsumer(String groupId) throws SQLException {
        this.consumer = new KafkaConsumer<>(KafkaConfig.consumerProps(groupId));
        this.customerService = new CustomerService();
        this.consumer.subscribe(Collections.singletonList(KafkaConfig.CUSTOMER_TOPIC));
    }

    @Override
    public void run() {
        try {
            while (!Thread.currentThread().isInterrupted()) {
                ConsumerRecords<String, Customer> records =
                        consumer.poll(Duration.ofMillis(1000));

                for (var record : records) {
                    Customer customer = record.value();
                    System.out.println("Получен клиент: " + customer);

                    // Сохранение в базу данных
                    try {
                        customerService.saveCustomer(customer);
                        System.out.println("Клиент сохранён в БД: " + customer.getId());
                    } catch (SQLException e) {
                        System.err.println("Ошибка сохранения клиента в БД: " + e.getMessage());
                        // В продакшене здесь нужно реализовать retry-логику или DLQ
                    }
                }

                // Коммит оффсетов после успешной обработки
                if (!records.isEmpty()) {
                    consumer.commitSync();
                }
            }
        } catch (Exception e) {
            if (!(e instanceof InterruptedException)) {
                e.printStackTrace();
            }
        } finally {
            try {
                customerService.close();
                consumer.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}
