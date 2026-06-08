class Department {
    var name: String
    var manager: Employee?
    
    init(name: String) {
        self.name = name
    }
}

class Employee {
    var name: String
    var department: Department?
    
    init(name: String) {
        self.name = name
    }
}

var itDepartment: Department? = Department(name: "IT")
var developer: Employee? = Employee(name: "Иван")

itDepartment?.manager = developer
developer?.department = itDepartment

itDepartment = nil
developer = nil
// Объекты не уничтожены — образовалась циклическая зависимость
