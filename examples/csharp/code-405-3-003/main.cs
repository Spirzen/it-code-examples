using System.Diagnostics;

// Практикум: https://spirzen.ru/encyclopedia/4-code-dev/4-05-asinhronnost/3

var urls = new (string Url, int DelayMs)[]
{
    ("https://example.com/page1", 2000),
    ("https://example.com/page2", 3500),
    ("https://example.com/page3", 1500),
    ("https://example.com/page4", 2500),
    ("https://example.com/page5", 1000),
};

Console.WriteLine("=== C# — последовательно, async и Parallel ===\n");

var seqTime = RunSequential(urls);
var asyncTime = await RunParallelAsync(urls);
var parallelCpuTime = RunParallelCpu();

Console.WriteLine("\n--- Итог ---");
Console.WriteLine($"Последовательно (I/O): {seqTime.TotalSeconds:F2} с");
Console.WriteLine($"async / WhenAll (I/O): {asyncTime.TotalSeconds:F2} с");
Console.WriteLine($"Parallel.ForEach (CPU): {parallelCpuTime.TotalSeconds:F2} с");

static TimeSpan RunSequential((string Url, int DelayMs)[] items)
{
    Console.WriteLine("1. ПОСЛЕДОВАТЕЛЬНО (Thread.Sleep блокирует поток)");
    var sw = Stopwatch.StartNew();
    foreach (var (url, delayMs) in items)
    {
        Thread.Sleep(delayMs);
        Console.WriteLine($"  Готово: {url}");
    }
    sw.Stop();
    Console.WriteLine($"  Время: {sw.Elapsed.TotalSeconds:F2} с\n");
    return sw.Elapsed;
}

static async Task<TimeSpan> RunParallelAsync((string Url, int DelayMs)[] items)
{
    Console.WriteLine("2. ПАРАЛЛЕЛЬНО (async / await + Task.WhenAll)");
    var sw = Stopwatch.StartNew();
    var tasks = items.Select(u => DownloadOneAsync(u.Url, u.DelayMs));
    await Task.WhenAll(tasks);
    sw.Stop();
    Console.WriteLine($"  Время: {sw.Elapsed.TotalSeconds:F2} с\n");
    return sw.Elapsed;
}

static async Task DownloadOneAsync(string url, int delayMs)
{
    await Task.Delay(delayMs);
    Console.WriteLine($"  Готово: {url}");
}

static TimeSpan RunParallelCpu()
{
    Console.WriteLine("3. CPU-BOUND (Parallel.ForEach по ядрам)");
    var files = Enumerable.Range(1, Environment.ProcessorCount * 2).ToArray();
    var sw = Stopwatch.StartNew();
    Parallel.ForEach(files, file => ProcessImage(file));
    sw.Stop();
    Console.WriteLine($"  Время: {sw.Elapsed.TotalSeconds:F2} с\n");
    return sw.Elapsed;
}

static void ProcessImage(int fileId)
{
    long sum = 0;
    for (int i = 0; i < 5_000_000; i++)
    {
        sum += i * i;
    }
    Console.WriteLine($"  Обработан файл #{fileId}, checksum={sum % 10_000}");
}
