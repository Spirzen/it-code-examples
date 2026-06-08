// src/main/java/ru/timur/crm/serializer/JsonDeserializer.java
package ru.timur.crm.serializer;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.kafka.common.serialization.Deserializer;
import ru.timur.crm.model.Customer;

import java.util.Map;

public class JsonDeserializer implements Deserializer<Customer> {
    private final ObjectMapper objectMapper = new ObjectMapper();

    @Override
    public void configure(Map<String, ?> configs, boolean isKey) {}

    @Override
    public Customer deserialize(String topic, byte[] data) {
        if (data == null) return null;
        try {
            return objectMapper.readValue(data, Customer.class);
        } catch (Exception e) {
            throw new RuntimeException("Error deserializing Customer from JSON", e);
        }
    }

    @Override
    public void close() {}
}
