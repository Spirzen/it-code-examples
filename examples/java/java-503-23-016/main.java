public class BlockedExample {
    private static final Object lock = new Object();
    
    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(() -> {
            synchronized (lock) {
                try {
                    Thread.sleep(2000); // удерживает монитор 2 секунды
                } catch (InterruptedException e) {}
            }
        });
        
        Thread t2 = new Thread(() -> {
            synchronized (lock) {
                System.out.println("Получил монитор");
            }
        });
        
        t1.start();
        Thread.sleep(100); // дать t1 время захватить монитор
        t2.start();
        
        Thread.sleep(100);
        System.out.println("Состояние t2: " + t2.getState()); // BLOCKED
    }
}
