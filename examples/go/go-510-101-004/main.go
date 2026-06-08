func TestConcurrentAccess(t *testing.T) {
    t.Parallel()
    
    var counter Counter
    var wg sync.WaitGroup
    
    for i := 0; i < 100; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            counter.Increment()
        }()
    }
    
    wg.Wait()
    if counter.Value() != 100 {
        t.Errorf("expected 100, got %d", counter.Value())
    }
}
