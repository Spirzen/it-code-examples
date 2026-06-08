class Shape {
    var color: String = "black"
    
    func draw() {
        print("Рисование фигуры цветом \(color)")
    }
    
    func area() -> Double {
        return 0.0
    }
}

class Circle: Shape {
    var radius: Double
    
    init(radius: Double) {
        self.radius = radius
        super.init()
    }
    
    override func draw() {
        print("Рисование круга радиусом \(radius) цветом \(color)")
    }
    
    override func area() -> Double {
        return Double.pi * radius * radius
    }
}

class Rectangle: Shape {
    var width: Double
    var height: Double
    
    init(width: Double, height: Double) {
        self.width = width
        self.height = height
        super.init()
    }
    
    override func draw() {
        print("Рисование прямоугольника \(width)x\(height) цветом \(color)")
    }
    
    override func area() -> Double {
        return width * height
    }
}
