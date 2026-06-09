class Animal {
    let name: String

    init(name: String) {
        self.name = name
    }

    func eat() {
        print("\(name) ест")
    }
}

class Cat: Animal {
    func speak() {
        print("Мяу!")
    }
}

class Dog: Animal {
    func speak() {
        print("Гав!")
    }
}

let cat = Cat(name: "Мурка")
let dog = Dog(name: "Шарик")
cat.eat()
cat.speak()
dog.eat()
dog.speak()
