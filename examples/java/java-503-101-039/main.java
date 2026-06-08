// Плохо: магические значения
public boolean isAdult(int age) {
    return age >= 18;
}

public void processOrder(Order order) {
    if (order.getStatus().equals("COMPLETED")) {
        // ...
    }
}

// Хорошо: именованные константы
private static final int ADULT_AGE_THRESHOLD = 18;
private static final String ORDER_STATUS_COMPLETED = "COMPLETED";

public boolean isAdult(int age) {
    return age >= ADULT_AGE_THRESHOLD;
}

public void processOrder(Order order) {
    if (order.getStatus().equals(ORDER_STATUS_COMPLETED)) {
        // ...
    }
}

// Ещё лучше: перечисления
public enum OrderStatus {
    PENDING, PROCESSING, COMPLETED, CANCELLED
}

public void processOrder(Order order) {
    if (order.getStatus() == OrderStatus.COMPLETED) {
        // ...
    }
}
