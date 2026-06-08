public class RaceConditionDemo {
    private static int sharedCounter = 0;

    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) sharedCounter++;
        });
        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) sharedCounter++;
        });

        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println("Ожидаемо: 2000, фактически: " + sharedCounter);
    }
}
