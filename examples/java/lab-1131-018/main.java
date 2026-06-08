import java.util.Scanner;

public class ReverseWords {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLinetrim();
        String[] words = line.split("\\s+");
        StringBuilder sb = new StringBuilder();
        for (int i = words.length - 1; i >= 0; i--) {
            if (sb.length() > 0) sb.append(' ');
            sb.append(words[i]);
        }
        System.out.println(sb);
        sc.close();
    }
}
