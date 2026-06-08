class SmartCache {
    constructor(maxSize = 100) {
        this.cache = new Map();
        this.maxSize = maxSize;
        this.registry = new FinalizationRegistry(key => {
            console.log(`Ключ ${key} удалён из кэша`);
        });
    }
    
    set(key, value) {
        if (this.cache.size >= this.maxSize) {
            const firstKey = this.cache.keys().next().value;
            this.cache.delete(firstKey);
        }
        
        this.cache.set(key, new WeakRef(value));
        this.registry.register(value, key);
    }
    
    get(key) {
        const ref = this.cache.get(key);
        return ref ? ref.deref() : undefined;
    }
    
    has(key) {
        return this.cache.has(key);
    }
    
    delete(key) {
        return this.cache.delete(key);
    }
    
    clear() {
        this.cache.clear();
        console.log("Кэш очищен");
    }
    
    size() {
        return this.cache.size;
    }
}

const cache = new SmartCache(3);
cache.set("user1", { name: "Иван" });
cache.set("user2", { name: "Мария" });
cache.set("user3", { name: "Алексей" });

console.log(cache.get("user1")); // { name: "Иван" }
console.log(cache.size());       // 3
