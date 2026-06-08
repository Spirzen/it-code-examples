// 1. Интерфейс - контракт поведения
interface Flyable {
    void fly(); // Абстрактный метод
    default void hover() { // Метод по умолчанию
        System.out.println("Летим с замиранием");
    }
}

// 2. Абстрактный класс - общий шаблон + часть реализации
abstract class Vehicle {
    protected String brand;

    public Vehicle(String brand) {
        this.brand = brand;
    }

    // Конкретный метод: общая логика для всех транспортных средств
    public void startEngine() {
        System.out.println(brand + ": Двигатель запущен");
    }

    // Абстрактный метод: должен быть реализован потомком
    public abstract void move(); 
}

// 3. Обычный класс - конкретная реализация
class Car extends Vehicle implements Flyable {
    
    private int wheels;

    public Car(String brand, int wheels) {
        super(brand);
        this.wheels = wheels;
    }

    @Override
    public void move() {
        System.out.println("Машина " + brand + " едет на " + wheels + " колесах");
    }

    @Override
    public void fly() {
        System.out.println("Машина " + brand + " летит (гипотетически)");
    }
}

// 4. Вложенные классы внутри внешнего класса Container
class Container {
    private String name;

    public Container(String name) {
        this.name = name;
    }

    // --- ОБЫЧНЫЙ ВНУТРЕННИЙ КЛАСС (Inner Class) ---
    // Имеет доступ ко всем полям и методам экземпляра Container
    class InnerClass {
        public void showInfo() {
            // Доступ к приватному полю внешнего класса
            System.out.println("Внутренний класс видит имя контейнера: " + name);
        }
    }

    // --- СТАТИЧЕСКИЙ ВНУТРЕННИЙ КЛАСС (Static Nested Class) ---
    // НЕ имеет доступа к экземпляру Container. Видит только статику.
    static class StaticNestedClass {
        // Нельзя обратиться к 'name' здесь, так как это не статика
        // public void showInfo() { System.out.println(name); } // Ошибка компиляции
        
        public void showInfo() {
            System.out.println("Статический вложенный класс работает изолированно.");
        }
        
        // Может использовать статические члены Container
        public void useStaticField() {
            // System.out.println(Container.STATIC_CONST); // Если бы он был
        }
    }
}

// Точка входа для демонстрации
public class Main {
    public static void main(String[] args) {
        
        // --- Пример 1: Наследование и Реализация ---
        // Создаем объект обычного класса, который наследует от абстрактного и реализует интерфейс
        Car myCar = new Car("Toyota", 4);
        myCar.startEngine(); // Вызов из родительского класса
        myCar.move();        // Реализация абстрактного метода
        myCar.fly();         // Реализация метода интерфейса
        myCar.hover();       // Использование метода по умолчанию из интерфейса

        // --- Пример 2: Обычный вложенный класс (Inner Class) ---
        Container container = new Container("Box-1");
        
        // Для создания объекта внутреннего класса нужен экземпляр внешнего
        Container.InnerClass inner = container.new InnerClass();
        inner.showInfo(); // Выведет имя контейнера, потому что есть ссылка на instance

        // --- Пример 3: Статический вложенный класс (Static Nested Class) ---
        // Создается напрямую, без экземпляра Container
        Container.StaticNestedClass staticObj = new Container.StaticNestedClass();
        staticObj.showInfo(); 
        
        // Попытка создать обычный вложенный класс без экземпляра родителя вызовет ошибку:
        // Container.InnerClass error = new Container.InnerClass(); // Не скомпилируется
    }
}
