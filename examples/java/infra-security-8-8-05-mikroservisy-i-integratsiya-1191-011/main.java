// src/main/java/ru/timur/crm/service/CustomerService.java
package ru.timur.crm.service;

import ru.timur.crm.config.DatabaseConfig;
import ru.timur.crm.model.Customer;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class CustomerService implements AutoCloseable {
    private final Connection connection;
    private final boolean manageConnection; // true = мы создали соединение, должны закрыть

    // Конструктор для внешнего соединения (рекомендуется для потребителя)
    public CustomerService(Connection existingConnection) {
        this.connection = existingConnection;
        this.manageConnection = false;
    }

    // Конструктор для создания нового соединения
    public CustomerService() throws SQLException {
        this.connection = DriverManager.getConnection(
                DatabaseConfig.DB_URL,
                DatabaseConfig.DB_USER,
                DatabaseConfig.DB_PASSWORD
        );
        this.manageConnection = true;
    }

    public void saveCustomer(Customer customer) throws SQLException {
        String sql = "INSERT INTO customers (id, name, email, phone) " +
                "VALUES (?, ?, ?, ?) " +
                "ON CONFLICT (id) DO UPDATE SET " +
                "name = EXCLUDED.name, " +
                "email = EXCLUDED.email, " +
                "phone = EXCLUDED.phone, " +
                "created_at = CURRENT_TIMESTAMP";

        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, customer.getId());
            stmt.setString(2, customer.getName());
            stmt.setString(3, customer.getEmail());
            stmt.setString(4, customer.getPhone());
            stmt.executeUpdate();
        }
    }

    @Override
    public void close() throws SQLException {
        if (manageConnection && connection != null && !connection.isClosed()) {
            connection.close();
        }
    }
}
