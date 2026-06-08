public class MemoryUsage {
    public static void main(String[] args) {
        Runtime runtime = Runtime.getRuntime();
        
        long usedMemory = runtime.totalMemory() - runtime.freeMemory();
        System.out.println("Используемая память: " + usedMemory / (1024 * 1024) + " MB");
        
        // Создание множества объектов для нагрузки кучи
        List<byte[]> memoryHog = new ArrayList<>();
        for (int i = 0; i < 1000; i++) {
            memoryHog.add(new byte[1024 * 1024]); // 1 MB каждый
        }
        
        usedMemory = runtime.totalMemory() - runtime.freeMemory();
        System.out.println("После выделения: " + usedMemory / (1024 * 1024) + " MB");
    }
}
