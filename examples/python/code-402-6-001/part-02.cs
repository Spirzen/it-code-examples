using System;
using System.Collections.Generic;

public class OrderProcessor
{
    public Dictionary<string, object> ProcessOrder(string orderId)
    {
        ValidateOrder(orderId);
        return CalculateAndSave(orderId);
    }

    private Dictionary<string, object> CalculateAndSave(string orderId)
    {
        // реализация
        return new Dictionary<string, object> { ["status"] = "processed" };
    }

    private void ValidateOrder(string orderId) { /* ... */ }
}
