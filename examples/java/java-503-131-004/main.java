
import java.io.*;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.List;

class Task {
    private int id;
    private String description;
    private boolean completed;

    public Task(int id, String description) {
        this.id = id;
        this.description = description;
        this.completed = false;
    }

    @Override
    public String toString() {
        return "{\"id\":" + id + ",\"description\":\"" + description + "\",\"completed\":" + completed + "}";
    }
    
    // Упрощенный метод для создания объекта из строки (для примера)
    public static Task fromJson(String jsonStr) {
        // В реальном проекте используйте JsonParser
        return null; 
    }
}

public class TaskTracker {
    private static final String FILE_PATH = "tasks.json";
    private List<Task> Задачи = new ArrayList<>();

    public void loadTasks() {
        Path path = Paths.get(FILE_PATH);
        if (Files.exists(path)) {
            try {
                String content = Files.readString(path);
                // Здесь должна быть логика парсинга JSON строки в объекты Task
                System.out.println("Задачи загружены (демо режим).");
            } catch (IOException e) {
                System.err.println("Ошибка чтения: " + e.getMessage());
            }
        }
    }

    public void saveTasks() {
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < Задачи.size(); i++) {
            sb.append(Задачи.get(i).toString());
            if (i < Задачи.size() - 1) sb.append(",");
        }
        sb.append("]");

        try {
            Files.writeString(Paths.get(FILE_PATH), sb.toString());
            System.out.println("Задачи сохранены.");
        } catch (IOException e) {
            System.err.println("Ошибка записи: " + e.getMessage());
        }
    }

    public void addTask(String desc) {
        int id = Задачи.size() > 0 ? Задачи.get(Задачи.size() - 1).getId() + 1 : 1;
        Задачи.add(new Task(id, desc));
    }

    public static void main(String[] args) {
        TaskTracker tracker = new TaskTracker();
        tracker.loadTasks();
        
        tracker.addTask("Купить продукты");
        tracker.addTask("Изучить Java");
        
        tracker.saveTasks();
    }
}
