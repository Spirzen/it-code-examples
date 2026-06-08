public class CacheService {
    // Плохо: синхронизированная коллекция
    private final Map<String, Object> syncMap = Collections.synchronizedMap(new HashMap<>());
    
    // Хорошо: конкурентная коллекция
    private final ConcurrentHashMap<String, Object> cache = new ConcurrentHashMap<>();
    
    public Object get(String key) {
        return cache.get(key);
    }
    
    public Object computeIfAbsent(String key, Function<String, Object> mappingFunction) {
        return cache.computeIfAbsent(key, mappingFunction);
    }
    
    public void put(String key, Object value) {
        cache.put(key, value);
    }
}
