// src/main/java/ru/timur/crm/producer/CustomerProducer.java
package ru.timur.crm.producer;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;
import ru.timur.crm.config.KafkaConfig;
import ru.timur.crm.model.Customer;

import java.util.concurrent.Future;

public class CustomerProducer implements AutoCloseable {
    private final KafkaProducer<String, Customer> producer;

    public CustomerProducer() {
        this.producer = new KafkaProducer<>(KafkaConfig.producerProps());
    }

    public Future<RecordMetadata> sendCustomerCreated(Customer customer) {
        ProducerRecord<String, Customer> record =
                new ProducerRecord<>(KafkaConfig.CUSTOMER_TOPIC, customer.getId(), customer);
        return producer.send(record);
    }

    @Override
    public void close() {
        producer.close();
    }
}
