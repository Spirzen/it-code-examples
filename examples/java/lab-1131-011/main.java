import java.util.*;

public class UniqueCount {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Set<Integer> seen = new HashSet<>();
        for (int i = 0; i < n; i++) {
            seen.add(sc.nextInt());
        }
        System.out.println(seen.size());
        sc.close();
    }
}
