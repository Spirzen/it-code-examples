class Figure {
    let name: String
    let color: String

    init(name: String, color: String) {
        self.name = name
        self.color = color
    }

    func describe() {
        print("Фигура «\(name)», цвет: \(color)")
    }
}

class Circle: Figure {
    init(color: String) {
        super.init(name: "Круг", color: color)
    }
}

class Square: Figure {
    init(color: String) {
        super.init(name: "Квадрат", color: color)
    }
}

let circle = Circle(color: "красный")
let square = Square(color: "синий")
circle.describe()
square.describe()
