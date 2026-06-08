public static class DistributedCacheExtensions
{
    public static async Task<T> GetAsync<T>(this IDistributedCache cache, string key)
    {
        var bytes = await cache.GetAsync(key);
        return bytes == null ? default : JsonSerializer.Deserialize<T>(bytes);
    }

    public static async Task SetAsync<T>(this IDistributedCache cache, string key, T value, DistributedCacheEntryOptions options)
    {
        var bytes = JsonSerializer.SerializeToUtf8Bytes(value);
        await cache.SetAsync(key, bytes, options);
    }
}
