import java.util.Scanner;

public class RangeSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
            pref[i + 1] = pref[i] + a[i];
        }
        int l = sc.nextInt();
        int r = sc.nextInt();
        System.out.println(pref[r + 1] - pref[l]);
        sc.close();
    }
}
