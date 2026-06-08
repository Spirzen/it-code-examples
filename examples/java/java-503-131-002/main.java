
import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.stream.Collectors;

public class TextSorter {
    public static void main(String[] args) {
        Path inputPath = Paths.get("input.txt");
        Path outputPath = Paths.get("output_sorted.txt");

        try {
            // Чтение всего содержимого файла
            String content = Files.readString(inputPath);
            
            // Разбиение на слова (по пробелам и знакам препинания)
            List<String> words = Arrays.stream(content.split("\\s+"))
                    .filter(word -> !word.isEmpty())
                    .collect(Collectors.toList());

            // Сортировка списка
            Collections.sort(words);

            // Запись результата
            String sortedContent = String.join("\n", words);
            Files.writeString(outputPath, sortedContent);

            System.out.println("Файл успешно отсортирован. Количество слов: " + words.size());

        } catch (IOException e) {
            System.err.println("Ошибка при работе с файлом: " + e.getMessage());
        }
    }
}
