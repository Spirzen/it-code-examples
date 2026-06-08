// src/main/java/ru/timur/crm/model/Customer.java
package ru.timur.crm.model;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Customer {
    private final String id;
    private final String name;
    private final String email;
    private final String phone;

    @JsonCreator
    public Customer(@JsonProperty("id") String id,
                    @JsonProperty("name") String name,
                    @JsonProperty("email") String email,
                    @JsonProperty("phone") String phone) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.phone = phone;
    }

    // Геттеры
    public String getId() { return id; }
    public String getName() { return name; }
    public String getEmail() { return email; }
    public String getPhone() { return phone; }

    @Override
    public String toString() {
        return "Customer{id='" + id + "', name='" + name +
                "', email='" + email + "', phone='" + phone + "'}";
    }
}
