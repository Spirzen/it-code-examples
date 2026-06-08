public class ChatHub : Hub
{
    public async Task SendMessage(string user, string message)
    {
        // Отправить всем клиентам
        await Clients.All.SendAsync("ReceiveMessage", user, message);

        // Отправить вызвавшему клиенту
        await Clients.Caller.SendAsync("Ack", "Delivered");

        // Отправить всем, кроме вызвавшего
        await Clients.Others.SendAsync("Notification", $"{user} wrote: {message}");
    }

    public override async Task OnConnectedAsync()
    {
        var connectionId = Context.ConnectionId;
        var userId = Context.UserIdentifier; // см. AddUserIdProvider
        await base.OnConnectedAsync();
    }

    public override async Task OnDisconnectedAsync(Exception? exception)
    {
        // Очистка ресурсов
        await base.OnDisconnectedAsync(exception);
    }
}
