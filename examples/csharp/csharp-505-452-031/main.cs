public class BackupJob : IJob
{
    private readonly IBackupService _backup;
    private readonly ILogger<BackupJob> _logger;

    public BackupJob(IBackupService backup, ILogger<BackupJob> logger)
    {
        _backup = backup;
        _logger = logger;
    }

    public async Task Execute(IJobExecutionContext context)
    {
        _logger.LogInformation("Starting backup at {Time}", DateTime.UtcNow);
        await _backup.RunAsync(context.CancellationToken);
        _logger.LogInformation("Backup completed");
    }
}
