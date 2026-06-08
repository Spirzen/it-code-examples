// 1. Транслятор: преобразование доменных объектов ↔ внешние форматы
internal class TaxRequestTranslator
{
    public string ToLegacyXml(TaxCalculationRequest request)
    {
        // Валидация и преобразование
        if (request.Amount <= 0) 
            throw new ArgumentException("Amount must be positive");
        
        return $@"<TaxRequest>
                    <Base>{request.Amount / (1 + request.TaxRate)}</Base>
                    <Rate>{request.TaxRate}</Rate>
                  </TaxRequest>";
    }

    public TaxCalculationResult FromLegacyXml(string xml)
    {
        var doc = XDocument.Parse(xml);
        var taxAmount = decimal.Parse(doc.Root.Element("TaxAmount").Value);
        // Внешняя система возвращает НДС отдельно — домен ожидает итог
        return new TaxCalculationResult(
            total: request.Amount + taxAmount, 
            tax: taxAmount
        );
    }
}

// 2. Адаптер + Защитный прокси
public class ResilientLegacyTaxAdapter : ITaxCalculator
{
    private readonly AccountingSystem _legacy;
    private readonly TaxRequestTranslator _translator;
    private readonly ILogger _logger;

    public ResilientLegacyTaxAdapter(
        AccountingSystem legacy,
        TaxRequestTranslator translator,
        ILogger<ResilientLegacyTaxAdapter> logger)
    {
        _legacy = legacy;
        _translator = translator;
        _logger = logger;
    }

    public async Task<TaxCalculationResult> Calculate(TaxCalculationRequest request)
    {
        // Circuit Breaker (через Polly)
        return await Policy
            .Handle<Exception>()
            .CircuitBreakerAsync(
                exceptionsAllowedBeforeBreaking: 3,
                durationOfBreak: TimeSpan.FromMinutes(1))
            .ExecuteAsync(async () => 
            {
                // Retry (тоже через Polly)
                return await Policy
                    .Handle<TimeoutException>()
                    .WaitAndRetryAsync(3, i => TimeSpan.FromSeconds(Math.Pow(2, i)))
                    .ExecuteAsync(async () => 
                    {
                        try
                        {
                            var xmlInput = _translator.ToLegacyXml(request);
                            var xmlOutput = await Task.Run(() => 
                                _legacy.CalcTax(xmlInput), 
                                CancellationToken.None);
                            return _translator.FromLegacyXml(xmlOutput);
                        }
                        catch (Exception ex)
                        {
                            _logger.LogWarning(ex, "Legacy tax calculation failed");
                            throw;
                        }
                    });
            });
    }
}

// 3. Фасад для клиента
public class TaxCalculationService
{
    private readonly ITaxCalculator _calculator;
    public TaxCalculationService(ITaxCalculator calculator) => _calculator = calculator;

    // Доменный метод — не знает о legacy
    public async Task<OrderWithTaxes> ApplyTaxesToOrder(Order order)
    {
        var taxRequest = new TaxCalculationRequest(
            amount: order.Total,
            taxRate: order.Country.TaxRate);

        var result = await _calculator.Calculate(taxRequest);
        
        return order.WithTaxes(
            totalInclTax: result.Total,
            taxAmount: result.Tax);
    }
}
