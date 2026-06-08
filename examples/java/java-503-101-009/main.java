// Плохо: метод выглядит как геттер, но изменяет состояние
public List<Order> getOrders() {
    if (orders == null) {
        orders = orderRepository.findByUserId(userId);
    }
    return orders;
}

// Хорошо: метод с побочным эффектом имеет соответствующее имя
public List<Order> loadOrders() {
    if (orders == null) {
        orders = orderRepository.findByUserId(userId);
    }
    return orders;
}

// Ещё лучше: разделить получение и загрузку
public List<Order> getOrders() {
    return orders; // может вернуть null или пустой список
}

public void loadOrders() {
    this.orders = orderRepository.findByUserId(userId);
}
