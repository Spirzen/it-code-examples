// Демонстрация различий между реализациями Set

import java.util.*;

public class SetExamples {
    public static void main(String[] args) {
        // HashSet: порядок не гарантируется, дубликаты запрещены
        Set<String> hashSet = new HashSet<>();
        hashSet.add("Java");
        hashSet.add("Python");
        hashSet.add("Java"); // Этот элемент будет проигнорирован
        System.out.println("HashSet размер: " + hashSet.size()); // Выведет 2
        
        // LinkedHashSet: сохраняет порядок вставки
        Set<String> linkedSet = new LinkedHashSet<>();
        linkedSet.add("First");
        linkedSet.add("Second");
        linkedSet.add("Third");
        System.out.println("LinkedHashSet порядок: " + linkedSet); // [First, Second, Third]
        
        // TreeSet: сортирует элементы естественным образом
        Set<Integer> treeSet = new TreeSet<>();
        treeSet.add(50);
        treeSet.add(10);
        treeSet.add(30);
        System.out.println("TreeSet отсортирован: " + treeSet); // [10, 30, 50]
    }
}
