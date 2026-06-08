// Плохо: класс управляет заказом и отправляет уведомления
public class Order {
    private Long id;
    private List<OrderItem> items;
    
    public void submit() {
        // логика подтверждения заказа
    }
    
    public void sendEmailNotification() {
        // логика отправки email
    }
    
    public void generatePdfInvoice() {
        // логика генерации PDF
    }
}

// Хорошо: разделение ответственности
public class Order {
    private Long id;
    private List<OrderItem> items;
    
    public void submit() {
        // логика подтверждения заказа
    }
}

public class NotificationService {
    public void sendOrderConfirmationEmail(Order order) {
        // логика отправки email
    }
}

public class InvoiceGenerator {
    public byte[] generatePdfInvoice(Order order) {
        // логика генерации PDF
    }
}
