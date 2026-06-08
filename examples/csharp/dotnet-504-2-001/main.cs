public class NotificationService : BackgroundService
{
    private readonly IHubContext<ChatHub> _hubContext;

    public NotificationService(IHubContext<ChatHub> hubContext)
    {
        _hubContext = hubContext;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            await _hubContext.Clients.All.SendAsync("SystemMessage", "Системное уведомление");
            await Task.Delay(TimeSpan.FromMinutes(1), stoppingToken);
        }
    }
}
