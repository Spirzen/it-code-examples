public class Animal {
    protected String name;

    protected Animal(String name) {
        this.name = name;
    }

    protected void makeSound() {
        System.out.println("Звук...");
    }
}

public class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    @Override
    protected void makeSound() {
        System.out.println(name + " лает!");
    }
}
