// Плохо: жирный интерфейс
public interface Worker {
    void work();
    void eat();
    void sleep();
    void attendMeeting();
    void writeReport();
}

// Хорошо: разделение интерфейсов
public interface Workable {
    void work();
}

public interface Breakable {
    void takeBreak();
}

public interface Reportable {
    void writeReport();
}

public class Programmer implements Workable, Breakable, Reportable {
    public void work() { /* реализация */ }
    public void takeBreak() { /* реализация */ }
    public void writeReport() { /* реализация */ }
}

public class Robot implements Workable {
    public void work() { /* реализация */ }
    // Роботу не нужно брать перерывы или писать отчёты
}
