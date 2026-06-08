// Цикломатическая сложность: 2 (хорошо)
public decimal CalculateDiscount(Order order, Customer customer, DateTime now)
{
    var baseDiscount = GetBaseDiscount(customer, order.Total);
    var dayBonus = GetDayBonus(now, order.Total);
    return order.Total * (baseDiscount + dayBonus);
}

private decimal GetBaseDiscount(Customer customer, decimal total)
{
    if (!customer.IsPremium) return 0;
    return total > 1000 ? 0.15m : 0.1m;
}

private decimal GetDayBonus(DateTime now, decimal total)
{
    if (total <= 1000) return 0;
    return now.DayOfWeek == DayOfWeek.Monday ? 0.05m : 0;
}
