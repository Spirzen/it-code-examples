public async Task<UserProfile> GetUserProfileAsync(int userId)
{
    var cacheKey = $"user:profile:{userId}";
    var cached = await _memcachedClient.GetAsync<UserProfile>(cacheKey);
    
    if (cached != null) return cached;

    // Промах → идём в БД
    var fromDb = await _userRepository.GetByIdAsync(userId);
    if (fromDb == null) return null;

    // Сохраняем в кэш с TTL = 5 минут
    await _memcachedClient.AddAsync(cacheKey, fromDb, TimeSpan.FromMinutes(5));

    return fromDb;
}

public async Task UpdateUserProfileAsync(int userId, UserProfile update)
{
    var result = await _userRepository.UpdateAsync(userId, update);
    if (result)
    {
        var cacheKey = $"user:profile:{userId}";
        // Вариант 1: перезапись
        await _memcachedClient.SetAsync(cacheKey, update, TimeSpan.FromMinutes(5));
        // Вариант 2: инвалидация (часто предпочтительнее)
        // await _memcachedClient.RemoveAsync(cacheKey);
    }
}
