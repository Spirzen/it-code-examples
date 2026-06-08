abstract class Animal {
    abstract void makeSound();  // абстрактный метод
}

class Dog extends Animal {
    void makeSound() {  // обязательная реализация
        System.out.println("Гав!");
    }
}
