trait Flyable {
    void fly() {
        println "Flying high!"
    }
}

trait Swimmable {
    void swim() {
        println "Swimming fast!"
    }
}

class Duck implements Flyable, Swimmable {}

def duck = new Duck()
duck.fly()  // Flying high!
duck.swim() // Swimming fast!
