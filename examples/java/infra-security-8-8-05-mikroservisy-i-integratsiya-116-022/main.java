
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.support.Acknowledgment;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.stereotype.Service;
import com.fasterxml.jackson.databind.ObjectMapper;

@Service
public class OrderEventConsumer {
    
    private final ObjectMapper objectMapper = new ObjectMapper();
    
    @KafkaListener(topics = "orders", groupId = "order-processing-group")
    public void consume(@Payload String eventData, Acknowledgment ack) {
        try {
            OrderEvent event = objectMapper.readValue(eventData, OrderEvent.class);
            
            System.out.println("Получено событие: " + event.type + 
                             " для заказа " + event.orderId);
            
            processEvent(event);
            
            // Подтверждение обработки
            ack.acknowledge();
            
        } catch (Exception e) {
            System.err.println("Ошибка обработки события: " + e.getMessage());
            // Можно отправить в DLQ
        }
    }
    
    private void processEvent(OrderEvent event) {
        switch (event.type) {
            case "OrderCreated":
                handleOrderCreated(event);
                break;
            case "OrderCompleted":
                handleOrderCompleted(event);
                break;
            default:
                System.out.println("Неизвестный тип события: " + event.type);
        }
    }
    
    private void handleOrderCreated(OrderEvent event) {
        System.out.println("Обработка созданного заказа: " + event.orderId);
        // Бизнес-логика...
    }
    
    private void handleOrderCompleted(OrderEvent event) {
        System.out.println("Обработка завершённого заказа: " + event.orderId);
        // Бизнес-логика...
    }
    
    private static class OrderEvent {
        public String type;
        public String orderId;
        public String customerId;
        public OrderItem[] items;
        public long timestamp;
    }
    
    private static class OrderItem {
        public String productId;
        public int quantity;
        public double price;
    }
}
