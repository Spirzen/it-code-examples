public class CounterService {
    // Плохо: блокировка на уровне метода
    private int counter = 0;
    
    public synchronized void increment() {
        counter++;
    }
    
    // Хорошо: использование атомарных операций
    private final AtomicInteger atomicCounter = new AtomicInteger(0);
    
    public void incrementAtomic() {
        atomicCounter.incrementAndGet();
    }
    
    // Ещё лучше: использование пула потоков
    private final ExecutorService executor = Executors.newFixedThreadPool(10);
    
    public CompletableFuture<Integer> asyncIncrement() {
        return CompletableFuture.supplyAsync(() -> {
            return atomicCounter.incrementAndGet();
        }, executor);
    }
}
