public class OrderProcessor
{
    public void ProcessOrder(Order order)
    {
        ValidateOrder(order);      // Вызов 1
        CalculateTotal(order);     // Вызов 2
        SaveOrder(order);          // Вызов 3
        SendConfirmation(order);   // Вызов 4
    }
    
    private void ValidateOrder(Order order)
    {
        CheckInventory(order);     // Вызов 1.1
        ValidateCustomer(order);   // Вызов 1.2
    }
    
    private void CheckInventory(Order order)
    {
        // Логика проверки наличия товаров
    }
}
