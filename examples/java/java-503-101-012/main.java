// Хорошо: try-with-resources
try (Connection connection = dataSource.getConnection();
     PreparedStatement statement = connection.prepareStatement(SQL)) {
    statement.setLong(1, userId);
    try (ResultSet resultSet = statement.executeQuery()) {
        while (resultSet.next()) {
            // обработка результата
        }
    }
} catch (SQLException e) {
    throw new DataAccessException("Failed to load user", e);
}

// Плохо: ресурсы могут не освободиться при возникновении исключения
Connection connection = null;
try {
    connection = dataSource.getConnection();
    // работа с соединением
} catch (SQLException e) {
    // обработка ошибки
} finally {
    if (connection != null) {
        try {
            connection.close(); // может выбросить исключение
        } catch (SQLException e) {
            logger.warn("Failed to close connection", e);
        }
    }
}
