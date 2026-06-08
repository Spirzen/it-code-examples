public interface IDbFactory
{
    IDbConnection CreateConnection();
    IDbCommand CreateCommand();
}

public class PostgresFactory : IDbFactory
{
    public IDbConnection CreateConnection() => new NpgsqlConnection();
    public IDbCommand CreateCommand() => new NpgsqlCommand();
}

public class SqlServerFactory : IDbFactory
{
    public IDbConnection CreateConnection() => new SqlConnection();
    public IDbCommand CreateCommand() => new SqlCommand();
}
