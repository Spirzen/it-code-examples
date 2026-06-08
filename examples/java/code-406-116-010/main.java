public class CacheLeak {
    private static final Map<String, byte[]> cache = new HashMap<>();
    
    public void addToCache(String key, byte[] Данные) {
        cache.put(key, Данные); // Данные накапливаются бесконечно
    }
    
    // Решение: использование WeakHashMap или ограничение размера
    private static final Map<String, byte[]> boundedCache = 
        Collections.synchronizedMap(new LinkedHashMap<>() {
            protected boolean removeEldestEntry(Map.Entry eldest) {
                return size() > 1000; // Ограничение 1000 элементов
            }
        });
}
