public class FactorialDebug {
    public static void main(String[] args) {
        int n = 5;
        long result = factorial(n);
        System.out.println(n + "! = " + result);
    }

    public static long factorial(int n) {
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }
}
