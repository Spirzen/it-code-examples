public class StackExample {
    public static void main(String[] args) {
        int x = 10;          // примитив в стеке main
        String s = "text";   // ссылка в стеке, объект в куче
        
        compute(5, 3);       // новый фрейм в стеке
    }
    
    static int compute(int a, int b) {
        int result = a * b;  // переменные в стеке compute
        return add(result, 10);
    }
    
    static int add(int x, int y) {
        return x + y;        // фрейм add поверх фрейма compute
    }
}
