// Демонстрация работы очередей и двусторонних очередей

import java.util.*;

public class QueueExamples {
    public static void main(String[] args) {
        // PriorityQueue: извлечение по приоритету (минимальный элемент первым)
        Queue<Integer> priorityQueue = new PriorityQueue<>();
        priorityQueue.offer(10);
        priorityQueue.offer(2);
        priorityQueue.offer(5);
        System.out.println("Приоритетный элемент: " + priorityQueue.poll()); // 2
        
        // Deque (ArrayDeque): работа как стек (LIFO) и очередь (FIFO)
        Deque<String> deque = new ArrayDeque<>();
        
        // Добавление в конец (как в очередь)
        deque.offerLast("A");
        deque.offerLast("B");
        
        // Добавление в начало (как в стек)
        deque.push("C"); 
        
        System.out.println("Последний элемент: " + deque.peekLast()); // B
        System.out.println("Первый элемент: " + deque.pop()); // C (удалено)
        
        // Очистка очереди
        while (!deque.isEmpty()) {
            System.out.print(deque.poll() + " ");
        }
    }
}
