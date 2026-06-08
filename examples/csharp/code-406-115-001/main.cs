public class OrderService
{
    private readonly ILogger _logger;
    private readonly int _unusedField = 42; // Неиспользуемое поле
    
    public OrderService(ILogger logger, IEmailService emailService)
    {
        _logger = logger;
        // emailService не используется — неиспользуемый параметр
    }
    
    public void ProcessOrder(Order order)
    {
        ValidateOrder(order);
        return; // Ранний возврат
        
        // Мёртвый код — никогда не выполнится
        SaveOrder(order);
        SendConfirmation(order);
    }
    
    private void UnusedMethod()
    {
        // Метод без вызовов
    }
}
