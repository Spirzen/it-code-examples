// Цикломатическая сложность: 8 (плохо)
public decimal CalculateDiscount(Order order, Customer customer, DateTime now)
{
    if (customer.IsPremium)
    {
        if (order.Total > 1000)
            return order.Total * 0.2m;
        else
            return order.Total * 0.15m;
    }
    else
    {
        if (order.Total > 1000)
        {
            if (now.DayOfWeek == DayOfWeek.Monday)
                return order.Total * 0.1m;
            else
                return order.Total * 0.05m;
        }
        else
        {
            return 0;
        }
    }
}
