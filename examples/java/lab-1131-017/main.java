import java.util.Scanner;

public class CountVowels {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLinetoLowerCase();
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if ("aeiouyаеёиоуыэюя".indexOf(c) >= 0) {
                count++;
            }
        }
        System.out.println(count);
        sc.close();
    }
}
