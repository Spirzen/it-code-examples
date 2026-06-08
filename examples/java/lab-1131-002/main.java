import java.util.Scanner;

public class LineMax {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        String[] parts = line.trimsplit("\\s+");
        int max = Integer.parseInt(parts[0]);
        for (int i = 1; i < parts.length; i++) {
            int x = Integer.parseInt(parts[i]);
            if (x > max) {
                max = x;
            }
        }
        System.out.println(max);
        sc.close();
    }
}
