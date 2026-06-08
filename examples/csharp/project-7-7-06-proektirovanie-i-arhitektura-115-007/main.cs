public class ConnectionService
{
    private readonly Func<Guid, string, string, UserConnection> _factory;
    
    public ConnectionService(
        Func<Guid, string, string, UserConnection> factory)
    {
        _factory = factory;
    }

    public async Task<UserConnection> CreateFromDbRecord(DbConnectionRecord record)
    {
        // Проверка, преобразование, логика — уже здесь
        if (string.IsNullOrWhiteSpace(record.Username))
            throw new ValidationException("Username required");
        
        return _factory(
            record.Id, 
            record.Username.Trim(), 
            record.ConnectionId.ToUpperInvariant()
        );
    }
}
