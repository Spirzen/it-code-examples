import java.math.BigDecimal;

class InventoryService {
    boolean checkStock(String productId) {
        return true;
    }
}

class PaymentService {
    boolean charge(String userId, BigDecimal amount) {
        return true;
    }
}

class ShippingService {
    String createShipment(String orderId, String address) {
        return "TRACK-" + orderId;
    }
}

class NotificationService {
    void sendOrderConfirmation(String userId, String trackingId) {
        System.out.println("Уведомление отправлено: " + trackingId);
    }
}

class OrderFacade {
    private final InventoryService inventory = new InventoryService();
    private final PaymentService payment = new PaymentService();
    private final ShippingService shipping = new ShippingService();
    private final NotificationService notification = new NotificationService();

    String placeOrder(String userId, String productId,
                      BigDecimal amount, String address) {
        if (!inventory.checkStock(productId)) {
            throw new IllegalStateException("Нет на складе");
        }
        if (!payment.charge(userId, amount)) {
            throw new IllegalStateException("Оплата не прошла");
        }
        String trackingId = shipping.createShipment(productId, address);
        notification.sendOrderConfirmation(userId, trackingId);
        return trackingId;
    }
}
