   public class DatabaseConfigurationProvider : ConfigurationProvider
   {
       private readonly IDbConnection _connection;
       
       public DatabaseConfigurationProvider(IDbConnection connection)
       {
           _connection = connection;
       }
       
       public override void Load()
       {
           data = _connection.Query("SELECT Key, Value FROM Config")
               .ToDictionary(x => x.Key, x => x.Value);
       }
   }
