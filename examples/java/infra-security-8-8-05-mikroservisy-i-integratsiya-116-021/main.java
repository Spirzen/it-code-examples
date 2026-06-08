
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.support.SendResult;
import org.springframework.stereotype.Service;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.UUID;
import java.util.concurrent.CompletableFuture;

@Service
public class OrderEventProducer {
    
    private final KafkaTemplate<String, String> kafkaTemplate;
    private final ObjectMapper objectMapper;
    private final String topic = "orders";
    
    public OrderEventProducer(KafkaTemplate<String, String> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
        this.objectMapper = new ObjectMapper();
    }
    
    public CompletableFuture<SendResult<String, String>> produceOrderCreated(
        UUID orderId, String customerId, OrderItem[] items) {
        
        try {
            OrderEvent event = new OrderEvent(
                "OrderCreated",
                orderId.toString(),
                customerId,
                items,
                System.currentTimeMillis()
            );
            
            String value = objectMapper.writeValueAsString(event);
            
            return kafkaTemplate.send(topic, orderId.toString(), value)
                .whenComplete((result, ex) -> {
                    if (ex == null) {
                        System.out.println("Событие отправлено: " + 
                            result.getRecordMetadata().offset());
                    } else {
                        System.err.println("Ошибка отправки: " + ex.getMessage());
                    }
                });
            
        } catch (Exception e) {
            throw new RuntimeException("Ошибка сериализации", e);
        }
    }
    
    private static class OrderEvent {
        public String type;
        public String orderId;
        public String customerId;
        public OrderItem[] items;
        public long timestamp;
        
        public OrderEvent(String type, String orderId, String customerId, 
                         OrderItem[] items, long timestamp) {
            this.type = type;
            this.orderId = orderId;
            this.customerId = customerId;
            this.items = items;
            this.timestamp = timestamp;
        }
    }
    
    private static class OrderItem {
        public String productId;
        public int quantity;
        public double price;
    }
}
