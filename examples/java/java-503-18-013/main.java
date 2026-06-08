interface Swimmable {
    default void swim() {
        System.out.println("Swimming...");
    }
}

interface Runnable {
    default void run() {
        System.out.println("Running...");
    }
}

// Класс может реализовать несколько интерфейсов
class Duck extends Animal implements Swimmable, Runnable {
    public Duck(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println("Quack!");
    }
}

// Использование
Duck duck = new Duck("Donald");
duck.swim(); // Swimming...
duck.run();  // Running...
duck.makeSound(); // Quack!
