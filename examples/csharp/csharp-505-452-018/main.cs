public class DiskSpaceCheck : IHealthCheck
{
    public async Task<HealthCheckResult> CheckHealthAsync(HealthCheckContext context, CancellationToken cancellationToken = default)
    {
        var drive = DriveInfo.GetDrives().First(d => d.IsReady && d.Name == "C:\\");
        var freePercent = (double)drive.AvailableFreeSpace / drive.TotalSize;

        if (freePercent < 0.1) // < 10%
            return HealthCheckResult.Unhealthy("Low disk space", null, new { FreePercent = freePercent });

        return HealthCheckResult.Healthy("Disk space OK");
    }
}

// Регистрация:
services.AddHealthChecks().AddCheck<DiskSpaceCheck>("disk");
