class Department {
    var name: String
    weak var university: University?
    
    init(name: String) {
        self.name = name
    }
}

class Professor {
    var name: String
    var department: Department?
    
    init(name: String) {
        self.name = name
    }
}

class Course {
    var title: String
    var professor: Professor?
    
    init(title: String) {
        self.title = title
    }
}
