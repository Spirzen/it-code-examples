public class ThreadExample {
    public static void main(String[] args) {
        // Создание потока через наследование
        MyThread thread1 = new MyThread("Поток-1");
        MyThread thread2 = new MyThread("Поток-2");
        
        // Запуск потоков
        thread1.start();
        thread2.start();
        
        // Ожидание завершения потоков
        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
        System.out.println("Все потоки завершены");
    }
    
    static class MyThread extends Thread {
        private String name;
        
        MyThread(String name) {
            this.name = name;
        }
        
        @Override
        public void run() {
            for (int i = 0; i < 5; i++) {
                System.out.println(name + ": итерация " + i);
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    break;
                }
            }
        }
    }
}
