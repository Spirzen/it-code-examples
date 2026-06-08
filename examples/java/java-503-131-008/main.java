
import java.io.IOException;
import java.nio.file.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class BackupUtility {
    public static void main(String[] args) {
        Path sourceDir = Paths.get("source_data");
        Path backupDir = Paths.get("backup_data");

        try {
            // Создание директории бэкапа, если её нет
            Files.createDirectories(backupDir);

            LocalDateTime now = LocalDateTime.now();
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd_HH-mm-ss");
            String timestamp = now.format(formatter);

            // Поиск всех файлов в источнике
            try (var stream = Files.list(sourceDir)) {
                stream.forEach(file -> {
                    try {
                        String fileName = file.getFileName().toString();
                        String nameWithoutExt = fileName.substring(0, fileName.lastIndexOf('.'));
                        String ext = fileName.substring(fileName.lastIndexOf('.'));
                        
                        Path newPath = backupDir.resolve(nameWithoutExt + "_" + timestamp + ext);
                        
                        Files.copy(file, newPath, StandardCopyOption.REPLACE_EXISTING);
                        System.out.println("Скопировано: " + fileName + " -> " + newPath.getFileName());
                    } catch (Exception e) {
                        System.err.println("Ошибка копирования " + file + ": " + e.getMessage());
                    }
                });
            }
        } catch (IOException e) {
            System.err.println("Критическая ошибка: " + e.getMessage());
        }
    }
}
