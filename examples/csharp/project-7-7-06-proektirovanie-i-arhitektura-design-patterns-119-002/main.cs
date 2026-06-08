public class CheckoutService
{
    private readonly IServiceProvider _serviceProvider;

    public CheckoutService(IServiceProvider serviceProvider)
    {
        _serviceProvider = serviceProvider;
    }

    public Task PayAsync(string userChoice)
    {
        var provider = _serviceProvider
            .GetRequiredKeyedService<IPaymentProvider>(userChoice);

        return provider.PayAsync();
    }
}
