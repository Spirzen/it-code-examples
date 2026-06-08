
import java.util.Scanner;

public class ConsoleCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.print("Введите первое число (или 'q' для выхода): ");
            String input1 = scanner.nextLine();

            if (input1.equalsIgnoreCase("q")) {
                break;
            }

            double num1 = Double.parseDouble(input1);
            System.out.print("Выберите операцию (+, -, *, /): ");
            String operation = scanner.nextLine();

            System.out.print("Введите второе число: ");
            double num2 = Double.parseDouble(scanner.nextLine());

            double result = 0;
            boolean validOperation = true;

            switch (operation) {
                case "+":
                    result = num1 + num2;
                    break;
                case "-":
                    result = num1 - num2;
                    break;
                case "*":
                    result = num1 * num2;
                    break;
                case "/":
                    if (num2 == 0) {
                        System.out.println("Ошибка: Деление на ноль!");
                        validOperation = false;
                    } else {
                        result = num1 / num2;
                    }
                    break;
                default:
                    System.out.println("Неверная операция.");
                    validOperation = false;
            }

            if (validOperation) {
                System.out.printf("Результат: %.2f%n", result);
            }
        }
        System.out.println("Программа завершена.");
        scanner.close();
    }
}
