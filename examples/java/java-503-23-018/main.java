public class ThreadStateTransitions {
    public static void main(String[] args) throws InterruptedException {
        Thread thread = new Thread(() -> {
            System.out.println("1. Состояние внутри run(): " + Thread.currentThread().getState());
            
            synchronized (this) {
                try {
                    wait(1000); // переход в TIMED_WAITING
                } catch (InterruptedException e) {}
            }
            
            System.out.println("2. После ожидания: " + Thread.currentThread().getState());
        });
        
        System.out.println("0. После создания: " + thread.getState()); // NEW
        
        thread.start();
        Thread.sleep(50);
        System.out.println("3. После start(): " + thread.getState()); // RUNNABLE или TIMED_WAITING
        
        thread.join();
        System.out.println("4. После завершения: " + thread.getState()); // TERMINATED
    }
}
