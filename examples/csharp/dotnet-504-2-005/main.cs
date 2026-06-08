// Models/ChatMessage.cs
public class ChatMessage
{
    public int Id { get; set; }
    public string UserId { get; set; } = string.Empty;
    public string UserName { get; set; } = string.Empty;
    public string Content { get; set; } = string.Empty;
    public DateTime Timestamp { get; set; }
    public string? TargetUserId { get; set; } // null — публичное, не null — приватное
    public string RoomName { get; set; } = "General";
}

// Models/UserStatus.cs
public class UserStatus
{
    public string UserId { get; set; } = string.Empty;
    public string UserName { get; set; } = string.Empty;
    public bool IsOnline { get; set; }
    public DateTime LastSeen { get; set; }
}
