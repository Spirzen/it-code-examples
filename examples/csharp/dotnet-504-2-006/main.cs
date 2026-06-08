// Services/IChatStore.cs
public interface IChatStore
{
    Task<List<ChatMessage>> GetMessagesAsync(string roomName, int limit = 50);
    Task SaveMessageAsync(ChatMessage message);
    Task<List<UserStatus>> GetOnlineUsersAsync();
    Task SetUserOnlineAsync(string userId, string userName);
    Task SetUserOfflineAsync(string userId);
}

// Services/InMemoryChatStore.cs
public class InMemoryChatStore : IChatStore
{
    private readonly List<ChatMessage> _messages = new();
    private readonly Dictionary<string, UserStatus> _userStatuses = new();

    public async Task<List<ChatMessage>> GetMessagesAsync(string roomName, int limit = 50)
    {
        return _messages
            .Where(m => m.RoomName == roomName)
            .OrderByDescending(m => m.Timestamp)
            .Take(limit)
            .Reverse()
            .ToList();
    }

    public async Task SaveMessageAsync(ChatMessage message)
    {
        _messages.Add(message);
    }

    public async Task<List<UserStatus>> GetOnlineUsersAsync()
    {
        return _userStatuses.Values.Where(u => u.IsOnline).ToList();
    }

    public async Task SetUserOnlineAsync(string userId, string userName)
    {
        _userStatuses[userId] = new UserStatus
        {
            UserId = userId,
            UserName = userName,
            IsOnline = true,
            LastSeen = DateTime.UtcNow
        };
    }

    public async Task SetUserOfflineAsync(string userId)
    {
        if (_userStatuses.TryGetValue(userId, out var status))
        {
            status.IsOnline = false;
            status.LastSeen = DateTime.UtcNow;
        }
    }
}
