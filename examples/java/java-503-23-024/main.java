public class VolatileFix {
    private static volatile boolean ready = false;
    private static int number = 0;
    
    public static void main(String[] args) throws InterruptedException {
        Thread writer = new Thread(() -> {
            number = 42;      // happens-before запись в volatile
            ready = true;     // volatile запись
        });
        
        Thread reader = new Thread(() -> {
            while (!ready) {  // volatile чтение
                // активное ожидание
            }
            // happens-after чтение volatile — number гарантированно 42
            System.out.println(number);
        });
        
        reader.start();
        writer.start();
    }
}
