open class Animal(val name: String) {
    fun eat() {
        println("$name ест")
    }
}

class Cat(name: String) : Animal(name) {
    fun speak() {
        println("Мяу!")
    }
}

class Dog(name: String) : Animal(name) {
    fun speak() {
        println("Гав!")
    }
}

fun main() {
    val cat = Cat("Мурка")
    val dog = Dog("Шарик")
    cat.eat()
    cat.speak()
    dog.eat()
    dog.speak()
}
