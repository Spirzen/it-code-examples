using System.Collections.Concurrent;
using System.Net.WebSockets;
using System.Text;
using System.Text.Json;

public sealed class OrderWebSocketHub
{
    private readonly ConcurrentDictionary<string, ConcurrentBag<WebSocket>> _byUser = new();

    public async Task HandleAsync(WebSocket socket, string userId, CancellationToken ct)
    {
        var bag = _byUser.GetOrAdd(userId, _ => new ConcurrentBag<WebSocket>());
        bag.Add(socket);
        var buffer = new byte[4096];
        try
        {
            while (socket.State == WebSocketState.Open && !ct.IsCancellationRequested)
            {
                var result = await socket.ReceiveAsync(buffer, ct);
                if (result.MessageType == WebSocketMessageType.Close) break;
                if (result.MessageType != WebSocketMessageType.Text) continue;

                var text = Encoding.UTF8.GetString(buffer, 0, result.Count);
                using var doc = JsonDocument.Parse(text);
                if (doc.RootElement.GetProperty("type").GetString() == "ping")
                    await SendAsync(socket, new { v = 1, type = "pong" }, ct);
            }
        }
        finally
        {
            await socket.CloseAsync(WebSocketCloseStatus.NormalClosure, "", ct);
        }
    }

    public async Task BroadcastToUserAsync(string userId, object message, CancellationToken ct)
    {
        if (!_byUser.TryGetValue(userId, out var bag)) return;
        foreach (var ws in bag)
            if (ws.State == WebSocketState.Open)
                await SendAsync(ws, message, ct);
    }

    private static Task SendAsync(WebSocket ws, object msg, CancellationToken ct)
    {
        var json = JsonSerializer.Serialize(msg);
        var bytes = Encoding.UTF8.GetBytes(json);
        return ws.SendAsync(bytes, WebSocketMessageType.Text, true, ct);
    }
}
