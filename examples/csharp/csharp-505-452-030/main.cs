[HttpGet("process")]
public async Task Process()
{
    var channel = Channel.CreateUnbounded<ProgressReport>();
    var writer = channel.Writer;

    _ = Task.Run(async () =>
    {
        try
        {
            await _progressService.ProcessDataAsync(new Progress<ProgressReport>(r => writer.TryWrite(r)), HttpContext.RequestAborted);
        }
        finally { writer.Complete(); }
    });

    Response.Headers.Append("Content-Type", "text/event-stream");
    await foreach (var report in channel.Reader.ReadAllAsync())
    {
        await Response.WriteAsync($"Данные: {JsonSerializer.Serialize(report)}\n\n");
        await Response.Body.FlushAsync();
    }
}
