public class SecondMaxDebug {
    public static void main(String[] args) {
        int[] numbers = {8, 3, 12, 5, 9, 1, 7};
        int result = findSecondMax(numbers);
        System.out.println("Второй максимум: " + result);
    }

    public static int findSecondMax(int[] array) {
        int max = array[0];
        int secondMax = Integer.MIN_VALUE;

        for (int i = 1; i < array.length; i++) {
            if (array[i] > max) {
                secondMax = max;
                max = array[i];
            } else if (array[i] > secondMax) {
                secondMax = array[i];
            }
        }
        return secondMax;
    }
}
