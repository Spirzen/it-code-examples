import java.util.Scanner;

public class MaxWithIndex {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int best = sc.nextInt();
        int pos = 1;
        for (int i = 2; i <= n; i++) {
            int x = sc.nextInt();
            if (x > best) {
                best = x;
                pos = i;
            }
        }
        System.out.println(best + " " + pos);
        sc.close();
    }
}
