protocol ShapeProtocol {
    func area() -> Double
    func perimeter() -> Double
    func draw()
}

class AbstractShape {
    func area() -> Double {
        fatalError("Метод area() должен быть переопределен")
    }
    
    func perimeter() -> Double {
        fatalError("Метод perimeter() должен быть переопределен")
    }
    
    func draw() {
        fatalError("Метод draw() должен быть переопределен")
    }
}

class Rectangle: AbstractShape {
    var width: Double
    var height: Double
    
    init(width: Double, height: Double) {
        self.width = width
        self.height = height
    }
    
    override func area() -> Double {
        return width * height
    }
    
    override func perimeter() -> Double {
        return 2 * (width + height)
    }
    
    override func draw() {
        print("Рисование прямоугольника \(width)x\(height)")
    }
}

class Ellipse: AbstractShape {
    var radiusX: Double
    var radiusY: Double
    
    init(radiusX: Double, radiusY: Double) {
        self.radiusX = radiusX
        self.radiusY = radiusY
    }
    
    override func area() -> Double {
        return Double.pi * radiusX * radiusY
    }
    
    override func perimeter() -> Double {
        return 2 * Double.pi * sqrt((radiusX * radiusX + radiusY * radiusY) / 2)
    }
    
    override func draw() {
        print("Рисование эллипса с радиусами \(radiusX) и \(radiusY)")
    }
}
