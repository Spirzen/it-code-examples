import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

/**
 * Демонстрация параллелизма в Java.
 * Практикум: https://spirzen.ru/encyclopedia/4-code-dev/4-05-asinhronnost/3
 */
public class ParallelismDemo {

    private static int sharedCounter = 0;

    public static void main(String[] args) throws InterruptedException {
        System.out.println("=== ДЕМОНСТРАЦИЯ ПАРАЛЛЕЛИЗМА В JAVA ===\n");

        demonstrateSimpleThreads();
        demonstrateRaceCondition();
        demonstrateSynchronization();
        demonstrateRunnable();
        demonstrateThreadPool();
    }

    private static void demonstrateSimpleThreads() throws InterruptedException {
        System.out.println("1. ПРОСТЫЕ ПОТОКИ:");

        Thread thread1 = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                System.out.println("  Поток 1: шаг " + i);
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        });

        Thread thread2 = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                System.out.println("  Поток 2: шаг " + i);
                try {
                    Thread.sleep(150);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        });

        thread1.start();
        thread2.start();
        thread1.join();
        thread2.join();
        System.out.println("  Все потоки завершены\n");
    }

    private static void demonstrateRaceCondition() throws InterruptedException {
        System.out.println("2. ГОНКА ДАННЫХ (Race Condition):");
        System.out.println("  Без синхронизации счётчик может быть неправильным!");

        sharedCounter = 0;
        Thread[] threads = new Thread[10];

        for (int i = 0; i < threads.length; i++) {
            threads[i] = new Thread(() -> {
                for (int j = 0; j < 1000; j++) {
                    sharedCounter++;
                }
            });
        }

        for (Thread t : threads) {
            t.start();
        }
        for (Thread t : threads) {
            t.join();
        }

        System.out.println("  Ожидаемое значение: 10000");
        System.out.println("  Фактическое значение: " + sharedCounter + "\n");
    }

    private static void demonstrateSynchronization() throws InterruptedException {
        System.out.println("3. СИНХРОНИЗАЦИЯ:");

        BankAccount account = new BankAccount(1000);
        Random random = new Random();

        Thread[] threads = new Thread[5];
        for (int i = 0; i < threads.length; i++) {
            final int threadId = i;
            threads[i] = new Thread(() -> {
                for (int j = 0; j < 5; j++) {
                    int amount = random.nextInt(100) + 1;
                    if (random.nextBoolean()) {
                        account.deposit(amount);
                        System.out.printf(
                                "  Поток %d: пополнил на %d, баланс: %d%n",
                                threadId,
                                amount,
                                account.getBalance());
                    } else {
                        account.withdraw(amount);
                        System.out.printf(
                                "  Поток %d: снял %d, баланс: %d%n",
                                threadId,
                                amount,
                                account.getBalance());
                    }
                    try {
                        Thread.sleep(50);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                    }
                }
            });
        }

        for (Thread t : threads) {
            t.start();
        }
        for (Thread t : threads) {
            t.join();
        }

        System.out.println("  Итоговый баланс: " + account.getBalance() + "\n");
    }

    private static void demonstrateRunnable() throws InterruptedException {
        System.out.println("4. ДЕМОНСТРАЦИЯ С RUNNABLE:");

        Runnable task = () -> {
            String name = Thread.currentThread().getName();
            for (int i = 1; i <= 3; i++) {
                System.out.println("  " + name + ": выполнение шага " + i);
                try {
                    Thread.sleep(200);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        };

        Thread t1 = new Thread(task, "Поток-A");
        Thread t2 = new Thread(task, "Поток-B");

        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println("  Runnable-задачи завершены\n");
    }

    private static void demonstrateThreadPool() throws InterruptedException {
        System.out.println("5. ПУЛ ПОТОКОВ (Thread Pool):");

        ExecutorService executor = Executors.newFixedThreadPool(3);

        for (int i = 1; i <= 6; i++) {
            final int taskId = i;
            executor.submit(() -> {
                String threadName = Thread.currentThread().getName();
                System.out.println("  Задача " + taskId + " выполняется в " + threadName);
                try {
                    Thread.sleep(300);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                System.out.println("  Задача " + taskId + " завершена в " + threadName);
            });
        }

        executor.shutdown();
        executor.awaitTermination(5, TimeUnit.SECONDS);
        System.out.println("  Все задачи из пула выполнены\n");
    }
}

class BankAccount {
    private int balance;

    BankAccount(int initialBalance) {
        this.balance = initialBalance;
    }

    synchronized void deposit(int amount) {
        balance += amount;
    }

    synchronized void withdraw(int amount) {
        if (balance >= amount) {
            balance -= amount;
        } else {
            System.out.println("  Недостаточно средств!");
        }
    }

    synchronized int getBalance() {
        return balance;
    }
}
