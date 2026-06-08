public class EventQueue {
    private final List<String> events = new ArrayList<>();
    private volatile boolean shutdown = false;
    
    public void addEvent(String event) {
        synchronized (events) {
            if (shutdown) throw new IllegalStateException("Очередь закрыта");
            events.add(event);
            events.notifyAll(); // happens-before пробуждение ожидающих потоков
        }
    }
    
    public String waitForEvent() throws InterruptedException {
        synchronized (events) {
            while (events.isEmpty() && !shutdown) {
                events.wait(); // освобождает монитор, блокируется
            }
            return events.isEmpty() ? null : events.remove(0);
        }
    }
    
    public void shutdown() {
        synchronized (events) {
            shutdown = true;
            events.notifyAll();
        }
    }
}
