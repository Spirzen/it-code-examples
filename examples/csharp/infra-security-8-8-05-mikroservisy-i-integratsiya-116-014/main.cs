using Confluent.Kafka;
using System.Text.Json;

public class OrderEventProducer
{
    private readonly IProducer<string, string> _producer;
    private readonly string _topic = "orders";

    public OrderEventProducer(string bootstrapServers)
    {
        var config = new ProducerConfig
        {
            BootstrapServers = bootstrapServers,
            Acks = Acks.All,
            EnableIdempotence = true,
            MaxInFlight = 5
        };

        _producer = new ProducerBuilder<string, string>(config).Build();
    }

    public async Task ProduceOrderCreatedAsync(Order order)
    {
        var eventData = new
        {
            type = "OrderCreated",
            orderId = order.Id,
            customerId = order.CustomerId,
            items = order.Items,
            timestamp = DateTimeOffset.UtcNow
        };

        var message = new Message<string, string>
        {
            Key = order.Id.ToString(),
            Value = JsonSerializer.Serialize(eventData)
        };

        try
        {
            var result = await _producer.ProduceAsync(_topic, message);
            Console.WriteLine($"Событие отправлено: {result.TopicPartitionOffset}");
        }
        catch (ProduceException<string, string> ex)
        {
            Console.WriteLine($"Ошибка отправки: {ex.Error.Reason}");
            throw;
        }
    }

    public void Dispose()
    {
        _producer?.Dispose();
    }
}
