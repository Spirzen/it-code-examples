import java.util.Scanner;

public class ArrayMin {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int min = sc.nextInt();
        for (int i = 1; i < n; i++) {
            int x = sc.nextInt();
            if (x < min) {
                min = x;
            }
        }
        System.out.println(min);
        sc.close();
    }
}
