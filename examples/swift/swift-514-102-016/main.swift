class Resource {
    let name: String
    
    init(name: String) {
        self.name = name
        print("Ресурс \(name) создан")
    }
    
    deinit {
        print("Ресурс \(name) уничтожен")
    }
    
    func use() {
        print("Использование ресурса \(name)")
    }
}

func demonstrateLifecycle() {
    let resource = Resource(name: "Файл")
    resource.use()
    // Ресурс будет уничтожен при выходе из функции
}

demonstrateLifecycle()
// Вывод:
// Ресурс Файл создан
// Использование ресурса Файл
// Ресурс Файл уничтожен
