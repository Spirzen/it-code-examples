   public class DataCleanupService : IHostedService
   {
       private readonly IServiceScopeFactory _scopeFactory;
       
       public DataCleanupService(IServiceScopeFactory scopeFactory)
       {
           _scopeFactory = scopeFactory;
       }
       
       public async Task StartAsync(CancellationToken ct)
       {
           using var scope = _scopeFactory.CreateScope();
           var dbContext = scope.ServiceProvider.GetRequiredService<AppDbContext>();
           await dbContext.CleanupOldDataAsync(ct);
       }
   }
