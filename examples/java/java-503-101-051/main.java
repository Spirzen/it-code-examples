@Service
public class OrderService {
    private final Counter ordersCreatedCounter;
    private final Timer orderProcessingTimer;
    private final Gauge activeOrdersGauge;
    
    public OrderService(MeterRegistry meterRegistry) {
        this.ordersCreatedCounter = Counter.builder("orders.created.total")
            .description("Total number of orders created")
            .tag("status", "success")
            .register(meterRegistry);
        
        this.orderProcessingTimer = Timer.builder("orders.processing.duration")
            .description("Time taken to process orders")
            .register(meterRegistry);
        
        this.activeOrdersGauge = Gauge.builder("orders.active.current", 
                orderRepository, repo -> repo.countActiveOrders())
            .description("Current number of active orders")
            .register(meterRegistry);
    }
    
    public Order createOrder(OrderRequest request) {
        return orderProcessingTimer.record(() -> {
            Order order = doCreateOrder(request);
            ordersCreatedCounter.increment();
            return order;
        });
    }
}
