public class ProgressService
{
    public async Task ProcessDataAsync(IProgress<ProgressReport> progress, CancellationToken ct)
    {
        var total = 100;
        for (int i = 0; i <= total; i++)
        {
            ct.ThrowIfCancellationRequested();
            await Task.Delay(50, ct);
            progress?.Report(new ProgressReport { PercentComplete = i, Message = $"Step {i}" });
        }
    }
}

public record ProgressReport(int PercentComplete, string Message);
