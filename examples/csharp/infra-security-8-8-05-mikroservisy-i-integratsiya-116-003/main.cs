using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using System.Net.WebSockets;
using System.Text;
using System.Text.Json;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllers();

var app = builder.Build();

// Middleware для обработки WebSocket
app.UseWebSockets(new WebSocketOptions
{
    KeepAliveInterval = TimeSpan.FromSeconds(30),
    ReceiveBufferSize = 4 * 1024
});

app.Map("/ws", async context =>
{
    if (!context.WebSockets.IsWebSocketRequest)
    {
        context.Response.StatusCode = StatusCodes.Status400BadRequest;
        return;
    }

    var webSocket = await context.WebSockets.AcceptWebSocketAsync();
    await HandleWebSocketConnection(webSocket);
});

app.Run();

async Task HandleWebSocketConnection(WebSocket webSocket)
{
    var clientId = Guid.NewGuid().ToString();
    var buffer = new byte[4096];
    
    Console.WriteLine($"Новое соединение: {clientId}");
    
    try
    {
        while (webSocket.State == WebSocketState.Open)
        {
            var result = await webSocket.ReceiveAsync(
                new ArraySegment<byte>(buffer), CancellationToken.None);
            
            if (result.MessageType == WebSocketMessageType.Close)
            {
                await webSocket.CloseAsync(
                    WebSocketCloseStatus.NormalClosure,
                    "Закрыто клиентом",
                    CancellationToken.None);
                break;
            }
            
            // Обработка текстового сообщения
            if (result.MessageType == WebSocketMessageType.Text)
            {
                var message = Encoding.UTF8.GetString(buffer, 0, result.Count);
                await ProcessMessage(webSocket, clientId, message);
            }
        }
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Ошибка соединения {clientId}: {ex.Message}");
    }
    finally
    {
        Console.WriteLine($"Соединение закрыто: {clientId}");
    }
}

async Task ProcessMessage(WebSocket socket, string clientId, string message)
{
    try
    {
        using var doc = JsonDocument.Parse(message);
        var root = doc.RootElement;
        
        if (!root.TryGetProperty("type", out var typeElement))
            return;
        
        var type = typeElement.GetString();
        
        switch (type)
        {
            case "ping":
                await SendMessage(socket, new
                {
                    type = "pong",
                    timestamp = DateTimeOffset.UtcNow.ToUnixTimeMilliseconds()
                });
                break;
                
            case "message":
                if (root.TryGetProperty("text", out var textElement))
                {
                    var response = new
                    {
                        type = "message",
                        clientId = clientId,
                        text = textElement.GetString(),
                        timestamp = DateTimeOffset.UtcNow.ToUnixTimeMilliseconds()
                    };
                    await SendMessage(socket, response);
                }
                break;
                
            default:
                await SendMessage(socket, new
                {
                    type = "error",
                    message = $"Неизвестный тип: {type}"
                });
                break;
        }
    }
    catch (JsonException ex)
    {
        await SendMessage(socket, new
        {
            type = "error",
            message = $"Ошибка парсинга JSON: {ex.Message}"
        });
    }
}

async Task SendMessage(WebSocket socket, object message)
{
    if (socket.State != WebSocketState.Open)
        return;
    
    var json = JsonSerializer.Serialize(message);
    var bytes = Encoding.UTF8.GetBytes(json);
    
    await socket.SendAsync(
        new ArraySegment<byte>(bytes),
        WebSocketMessageType.Text,
        true,
        CancellationToken.None);
}
