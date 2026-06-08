public class StringPoolStats {
    public static void main(String[] args) throws Exception {
        // Java 8: PermGen
        // Java 9+: Metaspace
        
        Class<?> clazz = Class.forName("java.lang.String");
        Field field = clazz.getDeclaredField("value");
        field.setAccessible(true);
        
        String sample = "test";
        char[] chars = (char[]) field.get(sample);
        System.out.println("Размер массива символов: " + chars.length);
    }
}
