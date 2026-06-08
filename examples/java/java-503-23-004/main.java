public class OldGenExample {
    // Статическая коллекция удерживает объекты в памяти
    private static List<byte[]> cache = new ArrayList<>();
    
    public static void main(String[] args) {
        for (int i = 0; i < 100; i++) {
            // Крупные объекты могут сразу попасть в Old Generation
            byte[] bigObject = new byte[1024 * 1024 * 5]; // 5 MB
            
            // Объекты, пережившие несколько сборок в Young,
            // перемещаются в Old Generation
            cache.add(bigObject);
            
            // Имитация работы приложения
            try { Thread.sleep(100); } catch (InterruptedException e) {}
        }
    }
}
