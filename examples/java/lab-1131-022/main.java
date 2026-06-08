import java.util.Scanner;

public class SimpleMenu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean running = true;
        while (running) {
            System.out.println("1 — привет  2 — квадрат числа  0 — выход");
            System.out.print("Выбор: ");
            String choice = sc.nextLinetrim();
            switch (choice) {
                case "1" -> System.out.println("Привет!");
                case "2" -> {
                    System.out.print("Число: ");
                    int x = Integer.parseInt(sc.nextLinetrim());
                    System.out.println(x * x);
                }
                case "0" -> running = false;
                default -> System.out.println("Неизвестная команда");
            }
        }
        sc.close();
    }
}
