// Хаб
public class ChatHub : Hub
{
    private readonly IChatService _chatService;

    public ChatHub(IChatService chatService)
    {
        _chatService = chatService;
    }

    public async Task SendMessage(string message)
    {
        var userId = Context.UserIdentifier;
        await _chatService.ProcessMessageAsync(userId, message);
    }
}

// Сервис
public class ChatService : IChatService
{
    private readonly IMessageRepository _repository;
    private readonly IHubContext<ChatHub> _hubContext;

    public ChatService(IMessageRepository repository, IHubContext<ChatHub> hubContext)
    {
        _repository = repository;
        _hubContext = hubContext;
    }

    public async Task ProcessMessageAsync(string userId, string content)
    {
        // Валидация, преобразование, сохранение
        var message = new Message { AuthorId = userId, Content = content, Timestamp = DateTime.UtcNow };
        await _repository.SaveAsync(message);

        // Рассылка события
        await _hubContext.Clients.All.SendAsync("NewMessage", message.AuthorId, message.Content);
    }
}
