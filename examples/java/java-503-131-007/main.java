
import java.io.IOException;
import java.nio.file.*;
import java.util.stream.Stream;

public class DirectoryScanner {
    public static void main(String[] args) {
        Path startPath = Paths.get("."); // Текущая директория

        try (Stream<Path> stream = Files.walk(startPath)) {
            stream
                .filter(Files::isRegularFile) // Только файлы
                .forEach(path -> {
                    long size = 0;
                    try {
                        size = Files.size(path);
                    } catch (IOException e) {
                        // Игнорирование ошибок доступа
                    }
                    System.out.printf("%s (%d байт)%n", path, size);
                });
        } catch (IOException e) {
            System.err.println("Ошибка сканирования: " + e.getMessage());
        }
    }
}
