// Hubs/ChatHub.cs
using Microsoft.AspNetCore.SignalR;

public class ChatHub : Hub
{
    private readonly IChatStore _chatStore;

    public ChatHub(IChatStore chatStore)
    {
        _chatStore = chatStore;
    }

    public override async Task OnConnectedAsync()
    {
        var userId = Context.UserIdentifier ?? Context.ConnectionId;
        var userName = Context.User?.Identity?.Name ?? "Anonymous";

        await _chatStore.SetUserOnlineAsync(userId, userName);
        await Clients.All.SendAsync("UserStatusChanged", new UserStatus
        {
            UserId = userId,
            UserName = userName,
            IsOnline = true,
            LastSeen = DateTime.UtcNow
        });

        await base.OnConnectedAsync();
    }

    public override async Task OnDisconnectedAsync(Exception? exception)
    {
        var userId = Context.UserIdentifier ?? Context.ConnectionId;
        await _chatStore.SetUserOfflineAsync(userId);

        await Clients.All.SendAsync("UserStatusChanged", new UserStatus
        {
            UserId = userId,
            IsOnline = false,
            LastSeen = DateTime.UtcNow
        });

        await base.OnDisconnectedAsync(exception);
    }

    public async Task JoinRoom(string roomName)
    {
        await Groups.AddToGroupAsync(Context.ConnectionId, roomName);
        var history = await _chatStore.GetMessagesAsync(roomName);
        await Clients.Caller.SendAsync("ReceiveHistory", history);
    }

    public async Task LeaveRoom(string roomName)
    {
        await Groups.RemoveFromGroupAsync(Context.ConnectionId, roomName);
    }

    public async Task SendMessage(string content, string roomName = "General")
    {
        var userId = Context.UserIdentifier ?? Context.ConnectionId;
        var userName = Context.User?.Identity?.Name ?? "Anonymous";

        var message = new ChatMessage
        {
            UserId = userId,
            UserName = userName,
            Content = content,
            Timestamp = DateTime.UtcNow,
            RoomName = roomName
        };

        await _chatStore.SaveMessageAsync(message);
        await Clients.Group(roomName).SendAsync("ReceiveMessage", message);
    }

    public async Task SendPrivateMessage(string content, string targetUserId)
    {
        var userId = Context.UserIdentifier ?? Context.ConnectionId;
        var userName = Context.User?.Identity?.Name ?? "Anonymous";

        var message = new ChatMessage
        {
            UserId = userId,
            UserName = userName,
            Content = content,
            Timestamp = DateTime.UtcNow,
            TargetUserId = targetUserId
        };

        await _chatStore.SaveMessageAsync(message);
        await Clients.User(targetUserId).SendAsync("ReceivePrivateMessage", message);
        await Clients.Caller.SendAsync("ReceivePrivateMessage", message); // эхо
    }
}
