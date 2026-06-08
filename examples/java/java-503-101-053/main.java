@Service
public class NotificationService {
    private final MessageSource messageSource;
    
    public NotificationService(MessageSource messageSource) {
        this.messageSource = messageSource;
    }
    
    public String getOrderCreatedMessage(Long orderId, Locale locale) {
        return messageSource.getMessage(
            "order.created",
            new Object[]{orderId},
            "Order #{0} created successfully", // сообщение по умолчанию
            locale
        );
    }
    
    public String getPaymentFailedMessage(String reason, Locale locale) {
        return messageSource.getMessage(
            "payment.failed",
            new Object[]{reason},
            "Payment failed: {0}",
            locale
        );
    }
}
