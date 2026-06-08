import java.util.Scanner;

public class Palindrome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLinereplaceAll("\\s+", "").toLowerCase();
        int left = 0;
        int right = s.length() - 1;
        boolean ok = true;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                ok = false;
                break;
            }
            left++;
            right--;
        }
        System.out.println(ok ? "YES" : "NO");
        sc.close();
    }
}
