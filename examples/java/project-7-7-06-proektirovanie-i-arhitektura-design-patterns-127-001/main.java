import java.util.ArrayList;
import java.util.List;

record OrderEvent(String orderId, String status) {}

interface OrderListener {
    void onOrderStatusChanged(OrderEvent event);
}

class OrderService {
    private final List<OrderListener> listeners = new ArrayList<>();

    void subscribe(OrderListener listener) {
        listeners.add(listener);
    }

    void changeStatus(String orderId, String newStatus) {
        OrderEvent event = new OrderEvent(orderId, newStatus);
        listeners.forEach(l -> l.onOrderStatusChanged(event));
    }
}

class WarehouseListener implements OrderListener {
    @Override
    public void onOrderStatusChanged(OrderEvent event) {
        if ("PAID".equals(event.status())) {
            System.out.println("Склад: начать сборку " + event.orderId());
        }
    }
}

class AnalyticsListener implements OrderListener {
    @Override
    public void onOrderStatusChanged(OrderEvent event) {
        System.out.println("Аналитика: статус " + event.status());
    }
}
