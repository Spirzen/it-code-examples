public class MemoryLeakExample
{
    private static readonly List<byte[]> _cache = new List<byte[]>();
    
    public void AddToCache()
    {
        // Добавляем данные в кэш, но никогда не удаляем старые
        _cache.Add(new byte[10 * 1024 * 1024]); // 10 МБ
    }
    
    // Правильный вариант с ограничением размера кэша
    public void AddToCacheWithLimit()
    {
        _cache.Add(new byte[10 * 1024 * 1024]);
        if (_cache.Count > 100)
        {
            _cache.RemoveRange(0, _cache.Count - 100); // Оставляем последние 100 элементов
        }
    }
}
