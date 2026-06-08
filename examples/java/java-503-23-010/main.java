public class MetaspaceExample {
    public static void main(String[] args) throws Exception {
        // Загрузка множества динамических классов
        for (int i = 0; i < 10000; i++) {
            ClassLoader loader = new CustomClassLoader();
            Class<?> clazz = loader.loadClass("DynamicClass" + i);
            System.out.println("Загружен класс: " + clazz.getName());
        }
    }
    
    static class CustomClassLoader extends ClassLoader {
        @Override
        protected Class<?> findClass(String name) throws ClassNotFoundException {
            // Генерация байт-кода для нового класса
            byte[] bytecode = generateBytecode(name);
            return defineClass(name, bytecode, 0, bytecode.length);
        }
        
        private byte[] generateBytecode(String name) {
            // Упрощённая генерация байт-кода
            return new byte[0];
        }
    }
}
