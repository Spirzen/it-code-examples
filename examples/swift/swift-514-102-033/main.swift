class Person {
    let name: String
    
    init(name: String) {
        self.name = name
        print("\(name) создан")
    }
    
    deinit {
        print("\(name) уничтожен")
    }
}

var person1: Person? = Person(name: "Анна")
var person2: Person? = person1
var person3: Person? = person1

person2 = nil
person3 = nil
person1 = nil
// Вывод:
// Анна создана
// Анна уничтожен
