// Демонстрация работы ArrayList (быстрый доступ по индексу)

import java.util.ArrayList;
import java.util.List;

public class ArrayListExample {
    public static void main(String[] args) {
        // Создаем список с начальной емкостью
        List<String> users = new ArrayList<>();
        
        // Добавление элементов
        users.add("Ivan");
        users.add("Maria");
        users.add("Alex");
        
        // Быстрый доступ по индексу O(1)
        System.out.println("Первый пользователь: " + users.get(0)); 
        
        // Вставка элемента в середину (медленная операция O(n))
        users.add(1, "NewUser");
        
        // Удаление элемента по индексу
        users.remove(0);
        
        // Итерация через цикл for (доступен только для List)
        for (int i = 0; i < users.size(); i++) {
            System.out.println(users.get(i));
        }
    }
}
