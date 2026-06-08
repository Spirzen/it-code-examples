public class Warrior {
    private String name;                 // приватное поле
    private static int count = 0;        // статическое поле (общее для всех)
    
    public Warrior(String name) {        // конструктор
        this.name = name;                // this обязателен
        count++;
    }
    
    public String getName() { return name; }           // геттер
    public void setName(String name) { this.name = name; }
    
    public static int getCount() { return count; }     // статический метод
    
    @Override
    public String toString() {            // переопределение метода Object
        return "Воин: " + name;
    }
}

// Наследование (один родитель)
class Knight extends Warrior {
    private String horseName;
    
    public Knight(String name, String horseName) {
        super(name);                     // вызов конструктора родителя — ОБЯЗАТЕЛЬНО
        this.horseName = horseName;
    }
    
    @Override
    public String toString() {           // переопределение
        return super.toString() + " на " + horseName;
    }
}

// Интерфейс (контракт)
interface Attackable {
    void attack(Warrior target);         // по умолчанию public abstract
}

// Реализация нескольких интерфейсов
class Paladin extends Warrior implements Attackable, Healable {
    public void attack(Warrior target) { /* ... */ }
    public void heal() { /* ... */ }
}
