import java.util.Scanner;

public class IsPrime {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        if (n < 2) {
            System.out.println("NO");
            sc.close();
            return;
        }
        boolean prime = true;
        for (long d = 2; d * d <= n; d++) {
            if (n % d == 0) {
                prime = false;
                break;
            }
        }
        System.out.println(prime ? "YES" : "NO");
        sc.close();
    }
}
