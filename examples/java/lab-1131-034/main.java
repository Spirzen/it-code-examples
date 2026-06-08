import java.util.Scanner;

public class CountWords {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLinetrim();
        if (line.isEmpty()) {
            System.out.println(0);
            sc.close();
            return;
        }
        String[] words = line.split("\\s+");
        System.out.println(words.length);
        sc.close();
    }
}
