public class JITExample {
    public static void main(String[] args) {
        // Первые 10 000 вызовов интерпретируются
        for (int i = 0; i < 10000; i++) {
            calculate(i);
        }
        // Последующие вызовы выполняются как нативный код
        for (int i = 10000; i < 20000; i++) {
            calculate(i);
        }
    }
    
    public static int calculate(int x) {
        return x * x + 2 * x + 1;
    }
}
