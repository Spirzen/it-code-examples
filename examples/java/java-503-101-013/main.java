// Хорошо: простая и понятная цепочка
List<String> activeUserEmails = users.stream()
    .filter(User::isActive)
    .map(User::getEmail)
    .collect(Collectors.toList());

// Плохо: излишне сложная цепочка
List<Order> orders = customers.stream()
    .filter(c -> c.getOrders() != null)
    .flatMap(c -> c.getOrders().stream())
    .filter(o -> o.getStatus() == OrderStatus.COMPLETED)
    .filter(o -> o.getCompletionDate() != null)
    .filter(o -> o.getCompletionDate().isAfter(LocalDate.now().minusMonths(1)))
    .sorted(Comparator.comparing(Order::getTotalAmount).reversed())
    .limit(10)
    .collect(Collectors.toList());
