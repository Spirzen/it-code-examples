public class PerformanceMonitor
{
    private readonly Stopwatch _stopwatch = new Stopwatch();
    private const long LatencyBudgetMs = 200;
    
    public async Task<T> ExecuteWithMonitoring<T>(Func<Task<T>> operation)
    {
        _stopwatch.Restart();
        var result = await operation();
        _stopwatch.Stop();
        
        var latency = _stopwatch.ElapsedMilliseconds;
        if (latency > LatencyBudgetMs)
        {
            _logger.LogWarning(
                "Превышен бюджет задержки: {Latency}мс > {Budget}мс",
                latency,
                LatencyBudgetMs
            );
        }
        
        return result;
    }
}
