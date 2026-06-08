using System;
using System.Threading;

foreach (Thread thread in Thread.CurrentThread.Thread.GetDomain().GetThreads())
{
    Console.WriteLine($"Поток: {thread.Name}, Статус: {thread.ThreadState}");
    // Получение стека вызовов доступно через Reflection или профилировщики
}
