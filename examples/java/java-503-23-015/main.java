public class RunnableExample {
    public static void main(String[] args) {
        // Создание задачи
        Task task1 = new Task("Задача-A");
        Task task2 = new Task("Задача-B");
        
        // Оборачивание задач в потоки
        Thread thread1 = new Thread(task1);
        Thread thread2 = new Thread(task2);
        
        thread1.start();
        thread2.start();
        
        // Использование лямбда-выражения (Java 8+)
        Thread lambdaThread = new Thread(() -> {
            System.out.println("Поток через лямбду запущен");
            for (int i = 0; i < 3; i++) {
                System.out.println("Лямбда: " + i);
                try { Thread.sleep(150); } catch (InterruptedException e) {}
            }
        });
        lambdaThread.start();
    }
    
    static class Task implements Runnable {
        private String name;
        
        Task(String name) {
            this.name = name;
        }
        
        @Override
        public void run() {
            for (int i = 0; i < 4; i++) {
                System.out.println(name + " выполняет шаг " + i);
                try {
                    Thread.sleep(200);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
        }
    }
}
