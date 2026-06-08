// Абстрактный класс "Транспорт"
abstract class Transport {
    private String name;  // поле

    public Transport(String name) {  // конструктор
        this.name = name;
    }

    // Абстрактный метод (без тела)
    public abstract void move();

    // Обычный метод
    public void honk() {
        System.out.println(name + " сигналит: Би-бип!");
    }
}

// Класс-наследник "Машина"
class Car extends Transport {
    public Car(String name) {
        super(name);  // вызываем конструктор родителя
    }

    // Реализация абстрактного метода
    @Override
    public void move() {
        System.out.println(getClass().getSimpleName() + " едет по дороге!");
    }
}

// Класс-наследник "Самолет"
class Airplane extends Transport {
    public Airplane(String name) {
        super(name);
    }

    @Override
    public void move() {
        System.out.println(getClass().getSimpleName() + " летит в небе!");
    }
}

public class Main {
    public static void main(String[] args) {
        Transport car = new Car("Toyota");
        Transport airplane = new Airplane("Boeing 747");

        car.move();       // Вывод: "Car едет по дороге!"
        car.honk();      // Вывод: "Toyota сигналит: Би-бип!"

        airplane.move();  // Вывод: "Airplane летит в небе!"
        airplane.honk();  // Вывод: "Boeing 747 сигналит: Би-бип!"
    }
}

