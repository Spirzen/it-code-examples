class Parent {
    func setup() {
        print("Родительская настройка")
    }
    
    func cleanup() {
        print("Родительская очистка")
    }
}

class Child: Parent {
    override func setup() {
        print("Дочерняя предварительная настройка")
        super.setup()
        print("Дочерняя дополнительная настройка")
    }
    
    override func cleanup() {
        print("Дочерняя предварительная очистка")
        super.cleanup()
        print("Дочерняя дополнительная очистка")
    }
}
