public class SynchronizedMethod {
    private int counter = 0;
    
    // Синхронизация на уровне экземпляра
    public synchronized void increment() {
        counter++;
    }
    
    // Синхронизация на уровне класса
    public static synchronized void staticIncrement() {
        // блокировка на классе SynchronizedMethod.class
    }
    
    public int getCounter() {
        return counter;
    }
    
    public static void main(String[] args) throws InterruptedException {
        SynchronizedMethod instance = new SynchronizedMethod();
        
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 10000; i++) instance.increment();
        });
        
        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 10000; i++) instance.increment();
        });
        
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        
        System.out.println("Итоговое значение: " + instance.getCounter()); // 20000
    }
}
