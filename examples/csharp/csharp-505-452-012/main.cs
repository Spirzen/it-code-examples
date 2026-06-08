public class OrderService
{
    private readonly ILogger<OrderService> _logger;
    public OrderService(ILogger<OrderService> logger) => _logger = logger;

    public void ProcessOrder(Order order)
    {
        _logger.LogInformation("Processing order {OrderId} for {CustomerId}", 
                               order.Id, order.CustomerId);

        try
        {
            // ...
        }
        catch (DbUpdateException ex)
        {
            _logger.LogError(ex, "Failed to save order {OrderId}", order.Id);
            throw;
        }
    }
}
