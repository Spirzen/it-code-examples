type Cache struct {
    mu sync.Mutex
    m  map[string]interface{}
}

func (c *Cache) Get(key string) (interface{}, bool) {
    c.mu.Lock()
    defer c.mu.Unlock()
    v, ok := c.m[key]
    return v, ok
}

func (c *Cache) Set(key string, val interface{}) {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.m[key] = val
}
