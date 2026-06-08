public class SynchronizedBlock {
    private final Object lock = new Object();
    private int value = 0;
    
    public void update(int newValue) {
        // Блокировка на частном объекте-замке
        synchronized (lock) {
            value = newValue;
        }
    }
    
    public void complexOperation() {
        // Блокировка на текущем экземпляре
        synchronized (this) {
            // критическая секция
        }
    }
    
    public static void classLevelOperation() {
        // Блокировка на классе
        synchronized (SynchronizedBlock.class) {
            // критическая секция для всего класса
        }
    }
}
