// Утечка памяти
public class MemoryLeak
{
    private static List<byte[]> _cache = new List<byte[]>();
    
    public void AddToCache()
    {
        // Добавляем данные, но никогда не удаляем
        _cache.Add(new byte[1024 * 1024]);  // 1MB
    }
}
