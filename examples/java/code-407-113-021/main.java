// Java (хороший пример)
interface NotificationService {
    void send(String message);
}

class EmailNotificationService implements NotificationService {
    public void send(String message) {
        System.out.println("Sending email: " + message);
    }
}

class SmsNotificationService implements NotificationService {
    public void send(String message) {
        System.out.println("Sending SMS: " + message);
    }
}

class OrderService {
    private final NotificationService notifier;

    public OrderService(NotificationService notifier) {
        this.notifier = notifier;
    }

    public void placeOrder(Order order) {
        // бизнес-логика
        notifier.send("Order placed!");
    }
}
