using RabbitMQ.Client;
using RabbitMQ.Client.Events;
using System.Text;
using System.Text.Json;
using NotificationService.Models;

namespace NotificationService.Services
{
    public class NotificationConsumer : IHostedService
    {
        private readonly ILogger<NotificationConsumer> _logger;
        private IConnection _connection;
        private IChannel _channel;
        private bool _running;

        public NotificationConsumer(ILogger<NotificationConsumer> logger)
        {
            _logger = logger;
        }

        public Task StartAsync(CancellationToken cancellationToken)
        {
            _running = true;
            
            var factory = new ConnectionFactory
            {
                HostName = "rabbitmq",
                UserName = "admin",
                Password = "secret_password"
            };

            _connection = factory.CreateConnection();
            _channel = _connection.CreateModel();
            _channel.QueueDeclare(queue: "order_events", durable: true, exclusive: false, autoDelete: false, arguments: null);

            var consumer = new EventingBasicConsumer(_channel);
            consumer.Received += async (model, ea) =>
            {
                var body = ea.Body.ToArray();
                var message = Encoding.UTF8.GetString(body);
                var orderEvent = JsonSerializer.Deserialize<OrderEvent>(message);
                
                await SendNotificationAsync(orderEvent);
                
                _channel.BasicAck(ea.DeliveryTag, false);
            };

            _channel.BasicConsume(queue: "order_events", autoAck: false, consumer: consumer);
            
            return Task.CompletedTask;
        }

        private async Task SendNotificationAsync(OrderEvent orderEvent)
        {
            using var client = new HttpClient();
            var content = new StringContent(JsonSerializer.Serialize(orderEvent), Encoding.UTF8, "application/json");
            
            try
            {
                var response = await client.PostAsync("http://localhost:8001/notify", content);
                _logger.LogInformation($"Notification sent for order {orderEvent.OrderId}: {response.StatusCode}");
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, $"Failed to send notification for order {orderEvent.OrderId}");
            }
        }

        public Task StopAsync(CancellationToken cancellationToken)
        {
            _running = false;
            _channel?.Close();
            _connection?.Close();
            return Task.CompletedTask;
        }
    }
}
