public class MaxFinder {
    public static void main(String[] args) {
        int[] data = {12, 45, 2, 89, 34};
        int max = data[0];
        
        for (int i = 1; i < data.length; i++) {
            if (data[i] > max) {
                max = data[i];
            }
        }
        
        System.out.println("Максимум: " + max); // Выведет: Максимум: 89
    }
}
