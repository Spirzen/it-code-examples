// Ограничение параллелизма: одновременно работает до 32 задач
var gate = new SemaphoreSlim(32);
var tasks = items.Select(async item =>
{
    await gate.WaitAsync(ct);
    try
    {
        await ProcessAsync(item, ct);
    }
    finally
    {
        gate.Release();
    }
});

await Task.WhenAll(tasks);
