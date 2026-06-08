// logger/ILogger.cs + Logger.cs
public interface ILogger
{
    void Info(string msg);
}

public class ConsoleLogger : ILogger
{
    public void Info(string msg) =>
        Console.WriteLine($"[INFO] {DateTime.UtcNow:O} {msg}");
}

// core/Order.cs + OrderService.cs
public record Order(int Id, string[] Items);

public class OrderService
{
    private readonly ILogger _logger;
    public OrderService(ILogger logger) => _logger = logger;

    public Order PlaceOrder(string[] items)
    {
        var order = new Order(1, items);
        _logger.Info($"Order {order.Id} placed with {items.Length} items");
        return order;
    }
}

// notification/IEmailService.cs + SmtpEmailService.cs
public interface IEmailService
{
    Task SendAsync(string to, string subject, string body);
}

public class SmtpEmailService : IEmailService
{
    private readonly ILogger _logger;
    public SmtpEmailService(ILogger logger) => _logger = logger;

    public async Task SendAsync(string to, string subject, string body)
    {
        _logger.Info($"Sending email to {to}");
        // ... SmtpClient
        await Task.CompletedTask;
    }
}

// app/Program.cs
using OrderSystem.Core;
using OrderSystem.Logger;
using OrderSystem.Notification;

var logger = new ConsoleLogger();
var orderService = new OrderService(logger);
var emailService = new SmtpEmailService(logger);

var order = orderService.PlaceOrder(["book", "pen"]);
await emailService.SendAsync("user@example.com", "Order confirmed", $"ID: {order.Id}");
