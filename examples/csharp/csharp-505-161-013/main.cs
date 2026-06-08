using System;

// Определение делегата
public delegate void MessageHandler(string message);

// Класс, генерирующий события
public class EventPublisher
{
    public event MessageHandler OnMessageReceived;

    public void Broadcast(string msg)
    {
        Console.WriteLine($"[{DateTime.Now:HH:mm:ss}] Отправлено сообщение: {msg}");
        OnMessageReceived?.Invoke(msg);
    }
}

// Класс, подписывающийся на события
public class Subscriber
{
    public void HandleMessage(string msg)
    {
        Console.WriteLine($"[{DateTime.Now:HH:mm:ss}] Получено: {msg}");
    }
}

class Program
{
    static void Main()
    {
        EventPublisher publisher = new EventPublisher();
        Subscriber sub1 = new Subscriber();
        Subscriber sub2 = new Subscriber();

        // Подписка на событие
        publisher.OnMessageReceived += sub1.HandleMessage;
        publisher.OnMessageReceived += sub2.HandleMessage;

        // Генерация события
        publisher.Broadcast("Привет, мир!");
        publisher.Broadcast("C# мощный язык!");

        // Отписка от события
        publisher.OnMessageReceived -= sub1.HandleMessage;
        publisher.Broadcast("Только второй подписчик услышит это.");
    }
}
