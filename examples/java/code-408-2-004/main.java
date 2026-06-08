// Интерфейс "Ремонтируемый"
interface Repairable {
    void repair();
}

// Абстрактный класс + интерфейс
abstract class Transport implements Repairable {
    public abstract void move();

    // Общий метод для всех наследников
    public void startEngine() {
        System.out.println("Двигатель запущен.");
    }
}

class Bicycle extends Transport {
    @Override
    public void move() {
        System.out.println("Велосипед едет!");
    }

    @Override
    public void repair() {
        System.out.println("Чиним цепь...");
    }
}

public class Main {
    public static void main(String[] args) {
        Bicycle bike = new Bicycle();
        bike.startEngine();  // Вывод: "Двигатель запущен." (наследовано)
        bike.move();         // Вывод: "Велосипед едет!"
        bike.repair();       // Вывод: "Чиним цепь..."
    }
}
