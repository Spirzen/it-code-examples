// Domain event как уведомление
public record OrderShippedEvent(OrderId Id) : INotification;

// Обработчик
public class EmailOnShippedHandler : INotificationHandler<OrderShippedEvent>
{
    public Task Handle(OrderShippedEvent ev, CancellationToken ct)
    {
        // Отправка email
        return _emailService.SendAsync($"Order {ev.Id} shipped", ct);
    }
}

// В сервисе
await _mediator.Publish(new OrderShippedEvent(order.Id), ct);
