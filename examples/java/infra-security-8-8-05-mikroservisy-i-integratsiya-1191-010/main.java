// src/main/java/ru/timur/crm/serializer/JsonSerializer.java
package ru.timur.crm.serializer;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.kafka.common.serialization.Serializer;
import ru.timur.crm.model.Customer;

import java.util.Map;

public class JsonSerializer implements Serializer<Customer> {
    private final ObjectMapper objectMapper = new ObjectMapper();

    @Override
    public void configure(Map<String, ?> configs, boolean isKey) {}

    @Override
    public byte[] serialize(String topic, Customer data) {
        try {
            return objectMapper.writeValueAsBytes(data);
        } catch (Exception e) {
            throw new RuntimeException("Error serializing Customer to JSON", e);
        }
    }

    @Override
    public void close() {}
}
