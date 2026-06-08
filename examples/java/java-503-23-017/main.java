public class WaitingExample {
    public static void main(String[] args) throws InterruptedException {
        Object monitor = new Object();
        
        Thread waiter = new Thread(() -> {
            synchronized (monitor) {
                try {
                    monitor.wait(); // ожидание без таймаута
                } catch (InterruptedException e) {}
            }
        });
        
        waiter.start();
        Thread.sleep(100);
        System.out.println("Состояние: " + waiter.getState()); // WAITING
    }
}
