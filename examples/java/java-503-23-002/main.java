public class NativeExample {
    // Объявление нативного метода
    public native int computeNative(int x, int y);
    
    static {
        // Загрузка нативной библиотеки
        System.loadLibrary("native-lib");
    }
    
    public static void main(String[] args) {
        NativeExample example = new NativeExample();
        int result = example.computeNative(5, 7);
        System.out.println("Результат из C: " + result);
    }
}
