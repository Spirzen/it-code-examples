   public class UserProfileService
   {
       private readonly IMemcachedClient _cache;
       private readonly IDbConnection _db;
       private readonly ILogger<UserProfileService> _logger;

       public UserProfileService(
           IMemcachedClient cache,
           IDbConnection db,
           ILogger<UserProfileService> logger)
       {
           _cache = cache ?? throw new ArgumentNullException(nameof(cache));
           _db = db ?? throw new ArgumentNullException(nameof(db));
           _logger = logger ?? throw new ArgumentNullException(nameof(logger));
       }

       public async Task<UserProfile?> GetUserAsync(int userId, CancellationToken ct = default)
       {
           // Формируем детерминированный ключ
           var cacheKey = $"user:profile:{userId}";

           // Пытаемся получить из кэша
           var cached = await _cache.GetAsync<UserProfile>(cacheKey, ct);
           if (cached != null)
               return cached;

           // Промах: читаем из БД
           UserProfile? fromDb = null;
           try
           {
               fromDb = await _db.QuerySingleOrDefaultAsync<UserProfile>(
                   "SELECT * FROM users WHERE id = @UserId", 
                   new { UserId = userId }, 
                   commandTimeout: 5, 
                   cancellationToken: ct);
           }
           catch (Exception ex) // БД недоступна — не падаем, пытаемся дальше
           {
               // Логируем, но не прерываем выполнение
               _logger.LogWarning(ex, "DB timeout for user {UserId}", userId);
               return null;
           }

           if (fromDb == null)
               return null;

           // Сохраняем в кэш с TTL = 5 минут
           // Используем `AddAsync`, чтобы не перезаписать, если другой поток уже записал
           await _cache.AddAsync(cacheKey, fromDb, TimeSpan.FromMinutes(5), ct);

           return fromDb;
       }

       public async Task UpdateUserAsync(UserProfile profile, CancellationToken ct = default)
       {
           // Сначала обновляем источник истины
           await _db.ExecuteAsync(
               "UPDATE users SET name = @Name, email = @Email WHERE id = @Id",
               profile, cancellationToken: ct);

           // Инвалидируем кэш (лучше, чем обновлять: избегаем гонок)
           await _cache.DeleteAsync($"user:profile:{profile.Id}", ct);
       }
   }
