@CompileStatic
class OrderService {
    
    @Autowired
    OrderRepository orderRepository
    
    @Autowired
    PaymentService paymentService
    
    @Transactional
    Order createOrder(OrderRequest request) {
        validateRequest(request)
        
        def order = new Order(
            userId: request.userId,
            items: request.items,
            status: 'PENDING',
            createdAt: new Date()
        )
        
        order = orderRepository.save(order)
        processPayment(order, request.paymentDetails)
        
        order.status = 'CONFIRMED'
        orderRepository.save(order)
        
        notificationService.sendOrderConfirmation(order)
        order
    }
    
    private void validateRequest(OrderRequest request) {
        assert request.userId, 'Идентификатор пользователя обязателен'
        assert request.items && !request.items.isEmpty(), 'Список товаров не может быть пустым'
        assert request.paymentDetails, 'Данные платежа обязательны'
    }
    
    private void processPayment(Order order, PaymentDetails details) {
        try {
            paymentService.charge(details, order.totalAmount)
        } catch (PaymentException e) {
            order.status = 'PAYMENT_FAILED'
            orderRepository.save(order)
            throw new OrderProcessingException('Ошибка обработки платежа', e)
        }
    }
}
