import java.util.Scanner;

public class Fibonacci {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long a = 1, b = 1;
        for (int i = 0; i < n; i++) {
            if (i > 0) System.out.print(" ");
            System.out.print(a);
            long next = a + b;
            a = b;
            b = next;
        }
        System.out.println();
        sc.close();
    }
}
