import java.util.*;

public class TwoSumExists {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        Set<Integer> seen = new HashSet<>();
        boolean found = false;
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            if (seen.contains(k - x)) {
                found = true;
                break;
            }
            seen.add(x);
        }
        System.out.println(found ? "YES" : "NO");
        sc.close();
    }
}
