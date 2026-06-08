public class OrderService
{
    public void CreateOrder(Order order, bool force = false)
    {
        if (!force)
        {
            ValidateOrder(order);
        }
        // Принудительное создание без валидации
        SaveOrder(order);
    }
    
    private void ValidateOrder(Order order)
    {
        if (order.Amount <= 0)
            throw new ValidationException("Сумма заказа должна быть положительной");
        if (string.IsNullOrWhiteSpace(order.CustomerName))
            throw new ValidationException("Имя клиента обязательно");
    }
}
