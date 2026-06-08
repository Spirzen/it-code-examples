class Animal {
    var name: String
    var age: Int
    
    init(name: String, age: Int) {
        self.name = name
        self.age = age
        print("Инициализация Animal")
    }
}

class Dog: Animal {
    var breed: String
    var isTrained: Bool
    
    init(name: String, age: Int, breed: String, trained: Bool) {
        self.breed = breed
        self.isTrained = trained
        super.init(name: name, age: age)
        print("Инициализация Dog")
    }
}

class GuideDog: Dog {
    var certificationNumber: String
    
    init(name: String, age: Int, breed: String, certification: String) {
        self.certificationNumber = certification
        super.init(name: name, age: age, breed: breed, trained: true)
        print("Инициализация GuideDog")
    }
}
