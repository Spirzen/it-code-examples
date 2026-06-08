using Microsoft.Extensions.Logging;

public class OrderService
{
    private readonly ILogger<OrderService> _logger;
    
    public OrderService(ILogger<OrderService> logger)
    {
        _logger = logger;
    }
    
    public async Task ProcessOrder(Order order)
    {
        _logger.LogInformation("Начало обработки заказа {OrderId}", order.Id);
        
        try
        {
            // Логируем входные данные
            _logger.LogDebug("Данные заказа: {@Order}", order);
            
            await ValidateOrder(order);
            await SaveOrder(order);
            
            _logger.LogInformation("Заказ {OrderId} успешно обработан", order.Id);
        }
        catch (ValidationException ex)
        {
            _logger.LogWarning(ex, "Ошибка валидации заказа {OrderId}", order.Id);
            throw;
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Критическая ошибка при обработке заказа {OrderId}", order.Id);
            throw;
        }
    }
}
