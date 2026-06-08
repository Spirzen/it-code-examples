public class HappensBeforeExamples {
    private int x = 0;
    private volatile boolean flag = false;
    
    public void example1() {
        // В пределах одного потока: порядок программы
        x = 1;      // A happens-before B
        x = 2;      // B
    }
    
    public void example2() {
        // Запись в volatile happens-before чтения этой переменной
        x = 10;     // A
        flag = true; // B (volatile запись) happens-before C
        
        // В другом потоке:
        // if (flag) { // C (volatile чтение) happens-before D
        //    System.out.println(x); // D — увидит 10
        // }
    }
    
    public synchronized void example3() {
        // Выход из synchronized блока happens-before входа другого потока
        x = 20;
    }
    
    public void example4() throws InterruptedException {
        Thread t = new Thread(() -> {
            x = 30; // A
        });
        
        t.start(); // start() happens-before начало run() — A виден в run()
        
        t.join();  // завершение run() happens-before возврат из join()
        // x == 30 гарантированно
    }
}
