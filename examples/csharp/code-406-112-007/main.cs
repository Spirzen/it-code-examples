public void ProcessOrder(Order order)
{
    _logger.LogTrace("Вход в ProcessOrder, OrderId: {OrderId}", order.Id);
    
    try
    {
        _logger.LogDebug("Валидация заказа");
        ValidateOrder(order);
        
        _logger.LogDebug("Сохранение заказа в БД");
        SaveToDatabase(order);
        
        _logger.LogDebug("Отправка уведомления");
        SendNotification(order);
        
        _logger.LogTrace("Выход из ProcessOrder, OrderId: {OrderId}", order.Id);
    }
    catch (Exception ex)
    {
        _logger.LogError(ex, "Ошибка в ProcessOrder, OrderId: {OrderId}", order.Id);
        throw;
    }
}
