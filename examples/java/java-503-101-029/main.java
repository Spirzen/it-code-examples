@Service
public class OrderService {
    private static final Logger logger = LoggerFactory.getLogger(OrderService.class);
    
    public Order createOrder(OrderRequest request) {
        logger.debug("Создание заказа: userId={}, items={}", 
            request.getUserId(), request.getItems().size());
        
        try {
            Order order = orderRepository.save(convert(request));
            logger.info("Заказ создан: orderId={}", order.getId());
            return order;
        } catch (ValidationException e) {
            logger.warn("Ошибка валидации при создании заказа: userId={}, error={}", 
                request.getUserId(), e.getMessage());
            throw e;
        } catch (Exception e) {
            logger.error("Ошибка создания заказа: userId={}", request.getUserId(), e);
            throw new OrderProcessingException("Failed to create order", e);
        }
    }
}
