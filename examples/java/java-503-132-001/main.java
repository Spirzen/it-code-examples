public class DebugExample {
    public static void main(String[] args) {
        int[] numbers = {5, 2, 8, 1, 9, 3};
        int max = findMax(numbers);          // breakpoint здесь
        System.out.println("Максимум: " + max);
    }

    public static int findMax(int[] array) {
        int max = array[0];
        for (int i = 0; i <= array.length; i++) {  // ошибка: <= вместо <
            if (array[i] > max) {
                max = array[i];
            }
        }
        return max;
    }
}
