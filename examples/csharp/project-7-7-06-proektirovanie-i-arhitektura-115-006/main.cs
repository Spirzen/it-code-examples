// Целевой интерфейс
public interface ITaxCalculator { decimal Calculate(Order order); }

// Адаптер для legacy
public class LegacyTaxAdapter : ITaxCalculator
{
    private readonly AccountingSystem _legacy;
    public decimal Calculate(Order order) {
        var xml = XmlSerializer.Serialize(order);
        var result = _legacy.CalcTax_V1(xml);
        return XmlSerializer.Deserialize<decimal>(result);
    }
}

// Адаптер для REST (будущее)
public class RestTaxAdapter : ITaxCalculator { ... }

// Фабрика
public class TaxCalculatorFactory
{
    public ITaxCalculator Create(string provider) => 
        provider switch {
            "legacy" => new LegacyTaxAdapter(),
            "rest" => new RestTaxAdapter(),
            _ => throw new ArgumentException()
        };
}
