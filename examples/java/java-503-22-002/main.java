String sql = "SELECT id, name, email FROM users WHERE created_after > ? AND status = ?";
try (PreparedStatement stmt = conn.prepareStatement(sql)) {
    stmt.setTimestamp(1, Timestamp.from(Instant.now().minus(Duration.ofDays(30))));
    stmt.setString(2, "ACTIVE");
    
    try (ResultSet rs = stmt.executeQuery()) {
        while (rs.next()) {
            long id = rs.getLong("id");
            String name = rs.getString("name");
            String email = rs.getString("email");
            // преобразование в доменный объект
        }
    }
}
