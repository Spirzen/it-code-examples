using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

[ApiController]
[Route("api/[controller]")]
public class EventsController : ControllerBase
{
    [HttpGet]
    public async Task GetEvents()
    {
        // Установка заголовков SSE
        Response.Headers.Append("Content-Type", "text/event-stream");
        Response.Headers.Append("Cache-Control", "no-cache");
        Response.Headers.Append("Connection", "keep-alive");
        
        // Отправка начального события
        await SendEventAsync("connected", new { message = "Подключено к потоку событий" });
        
        // Генерация событий в реальном времени
        var cancellationToken = HttpContext.RequestAborted;
        
        try
        {
            int eventId = 0;
            
            while (!cancellationToken.IsCancellationRequested)
            {
                // Отправка события каждые 2 секунды
                await SendEventAsync("tick", new
                {
                    id = Interlocked.Increment(ref eventId),
                    timestamp = DateTimeOffset.UtcNow.ToUnixTimeMilliseconds(),
                    message = $"Событие #{eventId}"
                });
                
                // Отправка события с указанием интервала повтора
                if (eventId == 1)
                {
                    await SendRetryAsync(5000); // 5 секунд
                }
                
                // Отправка комментария (игнорируется клиентом)
                await Response.WriteAsync($": Серверное время {DateTime.Now}\n\n");
                await Response.Body.FlushAsync(cancellationToken);
                
                await Task.Delay(2000, cancellationToken);
            }
        }
        catch (TaskCanceledException)
        {
            // Клиент закрыл соединение
            Console.WriteLine("Клиент отключился");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка потока: {ex.Message}");
        }
        finally
        {
            // Отправка финального события
            await SendEventAsync("disconnected", new { message = "Поток завершён" });
        }
    }
    
    [HttpGet("notifications")]
    public async Task GetNotifications()
    {
        Response.Headers.Append("Content-Type", "text/event-stream");
        Response.Headers.Append("Cache-Control", "no-cache");
        
        var cancellationToken = HttpContext.RequestAborted;
        
        // Получение последнего ID события из заголовка
        var lastEventId = Request.Headers["Last-Event-ID"].ToString();
        int lastId = string.IsNullOrEmpty(lastEventId) ? 0 : int.Parse(lastEventId);
        
        Console.WriteLine($"Восстановление с события #{lastId}");
        
        try
        {
            // Симуляция получения уведомлений из базы данных или очереди
            while (!cancellationToken.IsCancellationRequested)
            {
                var notifications = GetNewNotifications(lastId);
                
                foreach (var notification in notifications)
                {
                    await SendEventAsync("notification", new
                    {
                        id = notification.Id,
                        type = notification.Type,
                        title = notification.Title,
                        body = notification.Body,
                        timestamp = notification.Timestamp
                    }, notification.Id.ToString());
                    
                    lastId = notification.Id;
                }
                
                await Response.Body.FlushAsync(cancellationToken);
                await Task.Delay(1000, cancellationToken);
            }
        }
        catch (TaskCanceledException)
        {
            Console.WriteLine("Клиент отключился от уведомлений");
        }
    }
    
    /// <summary>
    /// Отправка события в формате SSE
    /// </summary>
    private async Task SendEventAsync(string eventType, object data, string id = null)
    {
        var sb = new StringBuilder();
        
        if (!string.IsNullOrEmpty(id))
        {
            sb.AppendLine($"id: {id}");
        }
        
        sb.AppendLine($"event: {eventType}");
        sb.AppendLine($"data: {System.Text.Json.JsonSerializer.Serialize(data)}");
        sb.AppendLine();
        
        await Response.WriteAsync(sb.ToString());
    }
    
    /// <summary>
    /// Установка интервала повторного подключения
    /// </summary>
    private async Task SendRetryAsync(int milliseconds)
    {
        await Response.WriteAsync($"retry: {milliseconds}\n\n");
    }
    
    /// <summary>
    /// Симуляция получения новых уведомлений
    /// </summary>
    private List<Notification> GetNewNotifications(int afterId)
    {
        // В реальном приложении: запрос к базе данных или очереди сообщений
        var notifications = new List<Notification>();
        
        // Пример генерации
        var random = new Random();
        if (random.Next(10) > 7)
        {
            notifications.Add(new Notification
            {
                Id = afterId + 1,
                Type = "info",
                Title = "Новое уведомление",
                Body = $"Случайное событие #{afterId + 1}",
                Timestamp = DateTimeOffset.UtcNow.ToUnixTimeMilliseconds()
            });
        }
        
        return notifications;
    }
    
    private class Notification
    {
        public int Id { get; set; }
        public string Type { get; set; }
        public string Title { get; set; }
        public string Body { get; set; }
        public long Timestamp { get; set; }
    }
}
