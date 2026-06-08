// Родительский класс
class Animal {
    protected String name;

    public Animal(String name) {
        this.name = name;
    }

    public void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

// Подкласс может наследовать только один суперкласс
class Dog extends Animal {
    public Dog(String name) {
        super(name); // вызов конструктора суперкласса
    }

    @Override
    public void makeSound() {
        System.out.println("Woof!");
    }
}
