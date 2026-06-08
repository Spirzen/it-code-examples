// C# (хороший пример)
public interface IDiscount
{
    decimal Apply(decimal amount);
}

public class SeasonalDiscount : IDiscount
{
    public decimal Apply(decimal amount) => amount * 0.9m;
}

public class VipDiscount : IDiscount
{
    public decimal Apply(decimal amount) => amount * 0.8m;
}

public class OrderCalculator
{
    public decimal CalculateTotal(IEnumerable<Item> items, IDiscount discount)
    {
        var total = items.Sum(item => item.Price);
        return discount.Apply(total);
    }
}
