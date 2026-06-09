class Animal {
    String name

    Animal(String name) {
        this.name = name
    }

    void eat() {
        println "${name} ест"
    }
}

class Cat extends Animal {
    Cat(String name) { super(name) }

    void speak() {
        println 'Мяу!'
    }
}

class Dog extends Animal {
    Dog(String name) { super(name) }

    void speak() {
        println 'Гав!'
    }
}

def cat = new Cat('Мурка')
def dog = new Dog('Шарик')
cat.eat()
cat.speak()
dog.eat()
dog.speak()
