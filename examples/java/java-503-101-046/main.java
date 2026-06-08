@Service
public class OrderService {
    private final OrderRepository orderRepository;
    private final PaymentService paymentService;
    private final NotificationService notificationService;
    
    public OrderService(
        OrderRepository orderRepository,
        PaymentService paymentService,
        NotificationService notificationService
    ) {
        this.orderRepository = Objects.requireNonNull(orderRepository);
        this.paymentService = Objects.requireNonNull(paymentService);
        this.notificationService = Objects.requireNonNull(notificationService);
    }
    
    public Order placeOrder(OrderRequest request) {
        // реализация
    }
}
