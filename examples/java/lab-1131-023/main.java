import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

public class GuessNumber {
    public static void main(String[] args) {
        int secret = ThreadLocalRandom.currentnextInt(1, 101);
        Scanner sc = new Scanner(System.in);
        System.out.println("Угадайте число от 1 до 100");
        while (true) {
            System.out.print("Ваш вариант: ");
            int guess = Integer.parseInt(sc.nextLinetrim());
            if (guess < secret) {
                System.out.println("Больше");
            } else if (guess > secret) {
                System.out.println("Меньше");
            } else {
                System.out.println("Верно!");
                break;
            }
        }
        sc.close();
    }
}
