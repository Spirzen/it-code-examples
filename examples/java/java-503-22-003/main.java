String sql = "INSERT INTO orders (user_id, amount, created_at) VALUES (?, ?, ?)";
try (PreparedStatement stmt = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {
    stmt.setLong(1, userId);
    stmt.setBigDecimal(2, amount);
    stmt.setTimestamp(3, Timestamp.from(Instant.now()));
    
    int rowsAffected = stmt.executeUpdate(); // возвращает количество изменённых строк
    
    // если нужно получить сгенерированный первичный ключ (например, SERIAL в PostgreSQL)
    try (ResultSet keys = stmt.getGeneratedKeys()) {
        if (keys.next()) {
            long orderId = keys.getLong(1);
            // использовать orderId
        }
    }
}
