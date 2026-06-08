// Domain event
public record OrderStatusChanged(OrderId Id, OrderStatus OldStatus, OrderStatus NewStatus);

// В агрегате Order
public void Ship() {
    if (Status != OrderStatus.Paid) throw new InvalidOperationException();
    var oldStatus = Status;
    Status = OrderStatus.Shipped;
    AddDomainEvent(new OrderStatusChanged(Id, oldStatus, Status));
}

// Обработчик события
public class NotificationHandler : IDomainEventHandler<OrderStatusChanged>
{
    private readonly IEmailService _email;
    private readonly ISmsService _sms;
    public Task Handle(OrderStatusChanged ev) {
        // Параллельно, с изоляцией ошибок
        _ = Task.Run(() => _email.Send(ev));
        _ = Task.Run(() => _sms.Send(ev));
        // Push — асинхронно через очередь
        _messageBus.Publish(new PushNotificationCommand(ev));
        return Task.CompletedTask;
    }
}
