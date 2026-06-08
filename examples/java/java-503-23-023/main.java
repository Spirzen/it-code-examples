public class VisibilityProblem {
    private static boolean ready = false;
    private static int number = 0;
    
    public static void main(String[] args) throws InterruptedException {
        Thread writer = new Thread(() -> {
            number = 42;      // запись 1
            ready = true;     // запись 2
        });
        
        Thread reader = new Thread(() -> {
            while (!ready) {  // чтение 1
                // активное ожидание
            }
            System.out.println(number); // чтение 2 — может вывести 0!
        });
        
        reader.start();
        writer.start();
    }
}
