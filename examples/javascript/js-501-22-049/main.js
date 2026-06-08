class CacheItem {
    constructor(value) {
        this.value = value;
        this.timestamp = Date.now();
    }
}

const cache = new Map();

function addToCache(key, value) {
    const item = new CacheItem(value);
    cache.set(key, new WeakRef(item));
    return item;
}

function getFromCache(key) {
    const ref = cache.get(key);
    if (ref) {
        return ref.deref();
    }
    return undefined;
}

const obj = addToCache("user1", { name: "Иван" });
console.log(getFromCache("user1")); // CacheItem { value: { name: "Иван" }, timestamp: ... }

// После удаления сильной ссылки объект может быть собран
obj = null;
setTimeout(() => {
    console.log(getFromCache("user1")); // undefined (возможно)
}, 100);
