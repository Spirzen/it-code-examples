// C# (хороший пример)
public interface INotificationService
{
    void Send(string message);
}

public class EmailNotificationService : INotificationService
{
    public void Send(string message)
    {
        Console.WriteLine($"Sending email: {message}");
    }
}

public class SmsNotificationService : INotificationService
{
    public void Send(string message)
    {
        Console.WriteLine($"Sending SMS: {message}");
    }
}

public class OrderService
{
    private readonly INotificationService _notifier;

    public OrderService(INotificationService notifier)
    {
        _notifier = notifier;
    }

    public void PlaceOrder(Order order)
    {
        // бизнес-логика
        _notifier.Send("Order placed!");
    }
}
