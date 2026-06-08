public class CacheService
{
    private readonly IMemoryCache _cache;
    public CacheService(IMemoryCache cache) => _cache = cache;

    public T GetOrCreate<T>(string key, Func<ICacheEntry, T> factory)
    {
        return _cache.GetOrCreate(key, entry =>
        {
            entry.AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(10);
            entry.Size = 1;
            return factory(entry);
        });
    }
}
