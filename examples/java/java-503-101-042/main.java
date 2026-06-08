// Доменное событие
public record OrderSubmittedEvent(
    OrderId orderId,
    CustomerId customerId,
    BigDecimal totalAmount,
    Instant occurredAt
) implements DomainEvent { }

// Генерация события в агрегате
public class Order {
    private final List<DomainEvent> events = new ArrayList<>();
    
    public void submit() {
        // бизнес-логика
        events.add(new OrderSubmittedEvent(id, customerId, total, Instant.now()));
    }
    
    public List<DomainEvent> getUncommittedEvents() {
        return new ArrayList<>(events);
    }
    
    public void markEventsAsCommitted() {
        events.clear();
    }
}

// Обработчик события
@Component
public class OrderNotificationHandler 
    implements DomainEventHandler<OrderSubmittedEvent> {
    
    private final EmailService emailService;
    
    @Override
    public void handle(OrderSubmittedEvent event) {
        emailService.sendOrderConfirmation(
            event.customerId(),
            event.orderId(),
            event.totalAmount()
        );
    }
}
