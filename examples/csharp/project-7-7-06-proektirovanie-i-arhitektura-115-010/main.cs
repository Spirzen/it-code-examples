// Регистрация с ключами
services.AddKeyedTransient<IPaymentStrategy, CardPaymentStrategy>("card");
services.AddKeyedTransient<IPaymentStrategy, SBPPaymentStrategy>("sbp");

// Использование
public class PaymentService
{
    private readonly IServiceProvider _sp;
    public PaymentService(IServiceProvider sp) => _sp = sp;

    public async Task ProcessPayment(string method, PaymentData Данные)
    {
        var strategy = _sp.GetRequiredKeyedService<IPaymentStrategy>(method);
        await strategy.ExecuteAsync(Данные);
    }
}
