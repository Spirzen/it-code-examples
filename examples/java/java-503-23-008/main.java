public class StringPoolExample {
    public static void main(String[] args) {
        // Строки-литералы разделяют один объект в пуле
        String s1 = "hello";
        String s2 = "hello";
        System.out.println(s1 == s2); // true — одна и та же ссылка
        
        // Создание через new — новый объект в куче
        String s3 = new String("hello");
        String s4 = new String("hello");
        System.out.println(s3 == s4); // false — разные объекты
        
        // Принудительное добавление в пул
        String s5 = s3.intern();
        System.out.println(s1 == s5); // true — теперь в пуле
        
        // Демонстрация экономии памяти
        List<String> literals = new ArrayList<>();
        for (int i = 0; i < 10000; i++) {
            literals.add("common-string"); // все ссылаются на один объект
        }
        
        List<String> news = new ArrayList<>();
        for (int i = 0; i < 10000; i++) {
            news.add(new String("common-string")); // 10000 отдельных объектов
        }
    }
}
