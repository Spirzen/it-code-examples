
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Создаем объект Scanner для чтения из стандартного ввода
        Scanner scanner = new Scanner(System.in);
        
        // Аналог input() для строки
        System.out.print("Введите имя: ");
        String name = scanner.nextLine();  // как input()
        
        // Аналог input() с преобразованием в число
        System.out.print("Введите возраст: ");
        int age = scanner.nextInt();  // как int(input())
        
        // Важно! nextInt() оставляет символ новой строки
        scanner.nextLine(); // очищаем буфер
        
        System.out.print("Введите город: ");
        String city = scanner.nextLine();
        
        // Чтение дробного числа
        System.out.print("Введите рост: ");
        double height = scanner.nextDouble();  // как float(input())
        
        scanner.close(); // закрываем scanner
    }
}
