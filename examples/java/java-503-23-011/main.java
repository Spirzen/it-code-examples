public class MetaspaceMonitor {
    public static void main(String[] args) {
        MemoryPoolMXBean metaspace = ManagementFactory.getMemoryPoolMXBeans()
            .stream()
            .filter(pool -> pool.getName().equals("Metaspace"))
            .findFirst()
            .orElse(null);
        
        if (metaspace != null) {
            MemoryUsage usage = metaspace.getUsage();
            System.out.println("Использовано Metaspace: " + usage.getUsed() / (1024 * 1024) + " MB");
            System.out.println("Максимум: " + usage.getMax() / (1024 * 1024) + " MB");
        }
    }
}
