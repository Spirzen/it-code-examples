public class SafeService {
    private final Object lockA = new Object();
    private final Object lockB = new Object();
    
    public void safeMethod() {
        // Всегда захватываем блокировки в одном порядке
        synchronized (lockA) {
            synchronized (lockB) {
                // Безопасная работа с ресурсами
            }
        }
    }
}
