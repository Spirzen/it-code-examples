class Animal {
    var name: String
    
    init(name: String) {
        self.name = name
    }
    
    func makeSound() {
        print("Животное издает звук")
    }
    
    func move() {
        print("Животное движется")
    }
}

class Dog: Animal {
    override func makeSound() {
        print("Гав-гав!")
    }
    
    override func move() {
        print("Собака бегает")
    }
}

class Cat: Animal {
    override func makeSound() {
        print("Мяу!")
    }
    
    override func move() {
        print("Кошка прыгает")
    }
}

class Bird: Animal {
    override func makeSound() {
        print("Чирик!")
    }
    
    override func move() {
        print("Птица летает")
    }
}

func demonstrateAnimals() {
    let animals: [Animal] = [
        Dog(name: "Рекс"),
        Cat(name: "Мурка"),
        Bird(name: "Чижик")
    ]
    
    for animal in animals {
        print("\(animal.name):")
        animal.makeSound()
        animal.move()
        print()
    }
}
