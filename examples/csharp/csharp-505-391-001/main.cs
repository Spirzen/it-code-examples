using var cts = new CancellationTokenSource();

var worker = new Thread(() =>
{
    while (!cts.Token.IsCancellationRequested)
    {
        Console.WriteLine("work");
        Thread.Sleep(500);
    }
    Console.WriteLine("exit");
});

worker.IsBackground = true;
worker.Start();

Thread.Sleep(2000);
cts.Cancel();
worker.Join();
