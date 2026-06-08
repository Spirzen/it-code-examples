public interface ICoffee
{
    decimal GetCost();
    string GetDescription();
}

public class SimpleCoffee : ICoffee
{
    public decimal GetCost() => 50;
    public string GetDescription() => "Кофе";
}

public abstract class CoffeeDecorator : ICoffee
{
    protected readonly ICoffee _coffee;
    public CoffeeDecorator(ICoffee coffee) => _coffee = coffee;

    public virtual decimal GetCost() => _coffee.GetCost();
    public virtual string GetDescription() => _coffee.GetDescription();
}

public class MilkDecorator : CoffeeDecorator
{
    public MilkDecorator(ICoffee coffee) : base(coffee) { }

    public override decimal GetCost() => base.GetCost() + 10;
    public override string GetDescription() => base.GetDescription() + ", с молоком";
}

public class SugarDecorator : CoffeeDecorator
{
    public SugarDecorator(ICoffee coffee) : base(coffee) { }

    public override decimal GetCost() => base.GetCost() + 5;
    public override string GetDescription() => base.GetDescription() + ", с сахаром";
}
