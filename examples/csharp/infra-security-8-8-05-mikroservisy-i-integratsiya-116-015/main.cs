using Confluent.Kafka;

public class OrderEventConsumer
{
    private readonly IConsumer<string, string> _consumer;
    private readonly string _topic = "orders";
    private readonly CancellationTokenSource _cts = new();

    public OrderEventConsumer(string bootstrapServers, string groupId)
    {
        var config = new ConsumerConfig
        {
            BootstrapServers = bootstrapServers,
            GroupId = groupId,
            AutoOffsetReset = AutoOffsetReset.Earliest,
            EnableAutoCommit = false,
            SessionTimeoutMs = 30000
        };

        _consumer = new ConsumerBuilder<string, string>(config)
            .SetPartitionsAssignedHandler((c, partitions) =>
            {
                Console.WriteLine($"Назначены партиции: {string.Join(',', partitions)}");
            })
            .Build();
    }

    public async Task StartAsync()
    {
        _consumer.Subscribe(_topic);

        try
        {
            while (!_cts.Token.IsCancellationRequested)
            {
                try
                {
                    var result = _consumer.Consume(_cts.Token);

                    Console.WriteLine($"Получено событие: {result.Message.Key}");
                    ProcessEvent(result.Message.Value);

                    // Подтверждение обработки
                    _consumer.Commit(result);
                }
                catch (ConsumeException ex)
                {
                    Console.WriteLine($"Ошибка потребления: {ex.Error.Reason}");
                }
            }
        }
        catch (OperationCanceledException)
        {
            Console.WriteLine("Потребление остановлено");
        }
        finally
        {
            _consumer.Close();
        }
    }

    private void ProcessEvent(string eventData)
    {
        // Обработка события
        Console.WriteLine($"Обработка: {eventData}");
    }

    public void Stop()
    {
        _cts.Cancel();
    }

    public void Dispose()
    {
        _consumer?.Dispose();
        _cts?.Dispose();
    }
}
