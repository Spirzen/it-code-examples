public class PostgresUserRepository : IUserRepository
{
    private readonly IDbConnection _db;
    
    public User? FindById(Guid id)
    {
        // Запрос JOIN users, user_profiles, user_settings
        // Маппинг в User (с Address, Preferences как Value Objects)
        // Возврат полного агрегата
    }
    
    public void Save(User user)
    {
        // BEGIN TX
        // INSERT/UPDATE users
        // INSERT/UPDATE user_profiles
        // INSERT/UPDATE user_settings
        // COMMIT
    }
}
