// Плохо: уязвимость к SQL-инъекции
public User findByEmail(String email) {
    String query = "SELECT * FROM users WHERE email = '" + email + "'";
    return jdbcTemplate.queryForObject(query, User.class);
}

// Хорошо: параметризованный запрос
public User findByEmail(String email) {
    String query = "SELECT * FROM users WHERE email = ?";
    return jdbcTemplate.queryForObject(query, new Object[]{email}, User.class);
}

// Ещё лучше: использование JPA
public Optional<User> findByEmail(String email) {
    return userRepository.findByEmail(email);
}
