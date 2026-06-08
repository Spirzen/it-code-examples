// Плохо: тесная связность
public class OrderService
{
    private readonly PaymentService _paymentService;
    private readonly InventoryService _inventoryService;
    private readonly NotificationService _notificationService;
    private readonly ReportingService _reportingService;
    // При изменении любого сервиса требуется пересборка OrderService
}

// Хорошо: слабая связность через интерфейсы
public class OrderService
{
    private readonly IPaymentGateway _paymentGateway;
    private readonly IInventory _inventory;
    private readonly INotification _notification;
    // Зависимость только от абстракций, не от реализаций
}
