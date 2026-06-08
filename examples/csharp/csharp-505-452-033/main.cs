public class DistributedBackgroundService : BackgroundService
{
    private readonly IDistributedLockFactory _lockFactory;

    public DistributedBackgroundService(IDistributedLockFactory lockFactory) 
        => _lockFactory = lockFactory;

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            using var lockHandle = await _lockFactory.CreateLock("backup-lock", TimeSpan.FromMinutes(10));
            if (await lockHandle.TryAcquireAsync(stoppingToken))
            {
                await DoWork(stoppingToken);
                await Task.Delay(TimeSpan.FromHours(24), stoppingToken); // следующий запуск
            }
            else
            {
                await Task.Delay(TimeSpan.FromMinutes(1), stoppingToken); // повторить позже
            }
        }
    }
}
