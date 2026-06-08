// Демонстрация работы Map и её реализаций

import java.util.*;

public class MapExamples {
    public static void main(String[] args) {
        // HashMap: быстрый доступ, порядок не гарантируется
        Map<String, Integer> scores = new HashMap<>();
        scores.put("Alice", 95);
        scores.put("Bob", 87);
        scores.put("Alice", 99); // Значение перезапишется
        System.out.println("Значение Alice: " + scores.get("Alice")); // 99
        
        // LinkedHashMap: сохраняет порядок вставки
        Map<String, String> history = new LinkedHashMap<>();
        history.put("Page1", "start");
        history.put("Page2", "middle");
        history.put("Page3", "end");
        System.out.println("История (порядок вставки): " + history.keySet());
        
        // TreeMap: сортировка по ключам
        Map<Integer, String> days = new TreeMap<>();
        days.put(3, "Wednesday");
        days.put(1, "Monday");
        days.put(2, "Tuesday");
        System.out.println("Дни недели (по возрастанию ключей): " + days);
    }
}
