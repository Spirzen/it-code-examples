public class DeadlockExample
{
    private readonly object _lock1 = new object();
    private readonly object _lock2 = new object();
    
    public void Method1()
    {
        lock (_lock1)
        {
            Thread.Sleep(100);  // Имитация работы
            lock (_lock2)       // Ожидание _lock2
            {
                Console.WriteLine("Method1 completed");
            }
        }
    }
    
    public void Method2()
    {
        lock (_lock2)
        {
            Thread.Sleep(100);  // Имитация работы
            lock (_lock1)       // Ожидание _lock1
            {
                Console.WriteLine("Method2 completed");
            }
        }
    }
    
    // Если вызвать оба метода в разных потоках одновременно,
    // произойдёт взаимоблокировка
}
