type CachedResolver struct {
    cache    map[string][]string
    mutex    sync.RWMutex
    resolver *net.Resolver
}

func (r *CachedResolver) Resolve(ctx context.Context, host string) ([]string, error) {
    // Чтение из кэша
    r.mutex.RLock()
    if addrs, ok := r.cache[host]; ok {
        r.mutex.RUnlock()
        return addrs, nil
    }
    r.mutex.RUnlock()
    
    // Разрешение и кэширование
    addrs, err := r.resolver.LookupHost(ctx, host)
    if err != nil {
        return nil, err
    }
    
    r.mutex.Lock()
    r.cache[host] = addrs
    r.mutex.Unlock()
    
    // Фоновое обновление каждые 30 секунд
    go r.periodicRefresh(host, 30*time.Second)
    
    return addrs, nil
}
