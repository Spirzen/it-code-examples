// Плохо: ConcurrentModificationException
for (User user : users) {
    if (!user.isActive()) {
        users.remove(user); // ошибка во время выполнения
    }
}

// Хорошо: использование итератора
Iterator<User> iterator = users.iterator();
while (iterator.hasNext()) {
    User user = iterator.next();
    if (!user.isActive()) {
        iterator.remove();
    }
}

// Альтернатива: создание новой коллекции
List<User> activeUsers = users.stream()
    .filter(User::isActive)
    .collect(Collectors.toList());
