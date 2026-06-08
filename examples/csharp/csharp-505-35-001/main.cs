public class OrderService
{
    private readonly ILogger _logger;
    private readonly IPaymentGateway _gateway;

    // Зависимости передаются через конструктор
    public OrderService(ILogger logger, IPaymentGateway gateway)
    {
        _logger = logger;
        _gateway = gateway;
    }

    public void ProcessOrder(Order order)
    {
        _logger.Log("Processing order...");
        _gateway.ProcessPayment(order.Total);
    }
}
