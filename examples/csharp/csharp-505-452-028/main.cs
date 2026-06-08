public class TimerHostedService : BackgroundService
{
    private readonly ILogger<TimerHostedService> _logger;
    private readonly IServiceScopeFactory _scopeFactory;
    private Timer? _timer;

    public TimerHostedService(ILogger<TimerHostedService> logger, IServiceScopeFactory scopeFactory)
    {
        _logger = logger;
        _scopeFactory = scopeFactory;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        _timer = new Timer(DoWork, null, TimeSpan.Zero, TimeSpan.FromMinutes(5));
        await Task.CompletedTask;
    }

    private void DoWork(object? state)
    {
        using var scope = _scopeFactory.CreateScope();
        var service = scope.ServiceProvider.GetRequiredService<IEmailService>();
        try
        {
            service.SendPendingEmails();
            _logger.LogInformation("Email batch sent at {Time}", DateTimeOffset.Now);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Failed to send emails");
        }
    }

    public override async Task StopAsync(CancellationToken cancellationToken)
    {
        _timer?.Change(Timeout.Infinite, 0);
        await base.StopAsync(cancellationToken);
    }

    protected override void Dispose(bool disposing)
    {
        _timer?.Dispose();
        base.Dispose(disposing);
    }
}
