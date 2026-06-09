class Animal {
    String name;

    Animal(String name) {
        this.name = name;
    }

    void eat() {
        System.out.println(name + " ест");
    }
}

class Cat extends Animal {
    Cat(String name) {
        super(name);
    }

    void speak() {
        System.out.println("Мяу!");
    }
}

class Dog extends Animal {
    Dog(String name) {
        super(name);
    }

    void speak() {
        System.out.println("Гав!");
    }
}

public class Main {
    public static void main(String[] args) {
        Cat cat = new Cat("Мурка");
        Dog dog = new Dog("Шарик");
        cat.eat();
        cat.speak();
        dog.eat();
        dog.speak();
    }
}
