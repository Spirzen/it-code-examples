class Person {
    var name: String
    var age: Int
    
    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }
}

var person1 = Person(name: "Алексей", age: 30)
var person2 = person1

person2.name = "Иван"
print(person1.name) // Вывод: Иван
print(person2.name) // Вывод: Иван
