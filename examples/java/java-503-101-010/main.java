// Плохо: использование исключений для управления потоком
try {
    User user = userRepository.findById(userId)
        .orElseThrow(() -> new UserNotFoundException(userId));
    processUser(user);
} catch (UserNotFoundException e) {
    // обработка отсутствия пользователя
    createUserDefaultProfile(userId);
}

// Хорошо: проверка условия перед действием
Optional<User> userOptional = userRepository.findById(userId);
if (userOptional.isPresent()) {
    processUser(userOptional.get());
} else {
    createUserDefaultProfile(userId);
}
