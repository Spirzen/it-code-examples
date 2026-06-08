// Явная проверка
if (user == null) {
    throw new IllegalArgumentException("Пользователь обязателен");
}

// Методы из Objects (Java 7+)

import java.util.Objects;

Objects.requireNonNull(user, "Пользователь обязателен");
String name = Objects.requireNonNullElse(user.getName(), "Без имени");

// Паттерн Optional (Java 8+)
Optional<User> optionalUser = userRepository.findById(userId);
String email = optionalUser
    .map(User::getEmail)
    .orElse("no-email@example.com");
