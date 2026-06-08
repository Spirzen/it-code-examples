// Интерфейс задаёт контракт: обязывает реализовать метод
interface IVoice {
    String makeSound();
}

// Абстрактный класс: хранит общие поля и поведение, но не создаётся напрямую
abstract class Animal implements IVoice {
    protected String name;

    public Animal(String name) {
        this.name = name;
    }

    // Абстрактный метод: реализация откладывается до наследников
    public abstract void move();
}

// Наследник 1
class Cat extends Animal {
    public Cat(String name) {
        super(name);
    }

    @Override
    public String makeSound() {
        return "Мяу!";
    }

    @Override
    public void move() {
        System.out.println(name + " крадётся.");
    }
}

// Наследник 2
class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    @Override
    public String makeSound() {
        return "Гав!";
    }

    @Override
    public void move() {
        System.out.println(name + " бежит.");
    }
}

// Точка входа
public class ZooLesson {
    public static void main(String[] args) {
        Animal cat = new Cat("Мурка");
        Animal dog = new Dog("Бобик");

        System.out.println(cat.makeSound());
        cat.move();

        System.out.println(dog.makeSound());
        dog.move();
    }
}
