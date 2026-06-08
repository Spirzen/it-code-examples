// Плохо: глубокая вложенность
public void processOrder(Order order) {
    if (order != null) {
        if (order.getItems() != null && !order.getItems().isEmpty()) {
            if (order.getCustomer() != null) {
                if (order.getCustomer().isActive()) {
                    // 5 уровней вложенности...
                }
            }
        }
    }
}

// Хорошо: ранний выход
public void processOrder(Order order) {
    if (order == null) {
        throw new IllegalArgumentException("Order cannot be null");
    }
    
    if (order.getItems() == null || order.getItems().isEmpty()) {
        throw new OrderValidationException("Order must have items");
    }
    
    if (order.getCustomer() == null) {
        throw new OrderValidationException("Customer is required");
    }
    
    if (!order.getCustomer().isActive()) {
        throw new OrderValidationException("Customer must be active");
    }
    
    // Основная логика
}
