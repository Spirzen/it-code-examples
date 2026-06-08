public class UserRepository
{
    private readonly string _connectionString;
    
    public UserRepository(string connectionString)
    {
        if (string.IsNullOrWhiteSpace(connectionString))
        {
            throw new ArgumentNullException(nameof(connectionString));
        }
        
        if (connectionString.Length > 4000)
        {
            throw new ArgumentException("Connection string exceeds maximum length", nameof(connectionString));
        }
        
        _connectionString = connectionString;
    }
}
