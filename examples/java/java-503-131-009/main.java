
import java.io.File;
import java.io.IOException;
import java.nio.file.*;

public class DiskSpaceMonitor {
    public static void main(String[] args) {
        File root = new File("/"); // Корневая директория
        
        try {
            FileStore store = FileSystems.getDefault().getFileStore(root.toPath());
            
            long totalSize = store.getTotalSpace();
            long usableSize = store.getUsableSpace();
            long usedSize = totalSize - usableSize;

            System.out.println("Диск: " + root.getAbsolutePath());
            System.out.println("Общий размер: " + formatBytes(totalSize));
            System.out.println("Занято: " + formatBytes(usedSize));
            System.out.println("Свободно: " + formatBytes(usableSize));
            System.out.println("Процент использования: " + (totalSize > 0 ? (usedSize * 100 / totalSize) : 0) + "%");

        } catch (IOException e) {
            System.err.println("Ошибка получения информации о диске: " + e.getMessage());
        }
    }

    private static String formatBytes(long bytes) {
        if (bytes < 1024) return bytes + " B";
        if (bytes < 1024 * 1024) return bytes / 1024 + " KB";
        if (bytes < 1024 * 1024 * 1024) return bytes / (1024 * 1024) + " MB";
        return bytes / (1024L * 1024 * 1024) + " GB";
    }
}
