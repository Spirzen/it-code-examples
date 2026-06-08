protocol Drawable {
    func draw()
    var area: Double { get }
}

class Circle: Drawable {
    var radius: Double
    
    init(radius: Double) {
        self.radius = radius
    }
    
    func draw() {
        print("Рисование круга радиусом \(radius)")
    }
    
    var area: Double {
        return Double.pi * radius * radius
    }
}

class Square: Drawable {
    var side: Double
    
    init(side: Double) {
        self.side = side
    }
    
    func draw() {
        print("Рисование квадрата со стороной \(side)")
    }
    
    var area: Double {
        return side * side
    }
}

class Triangle: Drawable {
    var base: Double
    var height: Double
    
    init(base: Double, height: Double) {
        self.base = base
        self.height = height
    }
    
    func draw() {
        print("Рисование треугольника")
    }
    
    var area: Double {
        return 0.5 * base * height
    }
}

func renderShapes(_ shapes: [Drawable]) {
    for shape in shapes {
        shape.draw()
        print("Площадь: \(shape.area)")
        print()
    }
}

let shapes: [Drawable] = [
    Circle(radius: 5.0),
    Square(side: 4.0),
    Triangle(base: 6.0, height: 8.0)
]

renderShapes(shapes)
