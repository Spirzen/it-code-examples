public class PaymentNotificationService : BackgroundService
{
    private readonly IHubContext<NotificationHub> _hubContext;
    private readonly IPaymentQueue _paymentQueue;

    public PaymentNotificationService(
        IHubContext<NotificationHub> hubContext,
        IPaymentQueue paymentQueue)
    {
        _hubContext = hubContext;
        _paymentQueue = paymentQueue;
    }

    protected override async Task ExecuteAsync(CancellationToken ct)
    {
        await foreach (var payment in _paymentQueue.ReadAsync(ct))
        {
            await _hubContext.Clients.User(payment.UserId)
                .SendAsync("PaymentCompleted", payment.Id, payment.Amount);
        }
    }
}
