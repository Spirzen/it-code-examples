// src/main/java/ru/timur/crm/App.java
package ru.timur.crm;

import ru.timur.crm.consumer.CustomerConsumer;
import ru.timur.crm.model.Customer;
import ru.timur.crm.producer.CustomerProducer;

import java.sql.SQLException;
import java.util.UUID;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class AppConsole {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newSingleThreadExecutor();

        try {
            // Запуск потребителя
            executor.submit(() -> {
                try {
                    new CustomerConsumer("crm-group-1").run();
                } catch (SQLException e) {
                    System.err.println("Ошибка инициализации потребителя: " + e.getMessage());
                }
            });

            // Отправка тестовых данных
            try (CustomerProducer producer = new CustomerProducer()) {
                for (int i = 1; i <= 3; i++) {
                    Customer customer = new Customer(
                            UUID.randomUUID().toString(),
                            "Клиент " + i,
                            "client" + i + "@example.com",
                            "+7900123456" + i
                    );

                    try {
                        var metadata = producer.sendCustomerCreated(customer).get();
                        System.out.println("Отправлено в партицию " +
                                metadata.partition() + ", смещение " + metadata.offset());
                    } catch (Exception e) {
                        System.err.println("Ошибка отправки: " + e.getMessage());
                    }

                    Thread.sleep(1000);
                }
            }

            // Даем время обработать сообщения
            Thread.sleep(5000);

        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            executor.shutdownNow();
        }
    }
}
