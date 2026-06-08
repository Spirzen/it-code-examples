import java.util.*;

public class UniqueOrdered {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        LinkedHashSet<Integer> set = new LinkedHashSet<>();
        for (int i = 0; i < n; i++) {
            set.add(sc.nextInt());
        }
        boolean first = true;
        for (int x : set) {
            if (!first) System.out.print(" ");
            System.out.print(x);
            first = false;
        }
        System.out.println();
        sc.close();
    }
}
