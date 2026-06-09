class Figure {
    String name
    String color

    Figure(String name, String color) {
        this.name = name
        this.color = color
    }

    void describe() {
        println "Фигура «${name}», цвет: ${color}"
    }
}

class Circle extends Figure {
    Circle(String color) {
        super('Круг', color)
    }
}

class Square extends Figure {
    Square(String color) {
        super('Квадрат', color)
    }
}

def circle = new Circle('красный')
def square = new Square('синий')
circle.describe()
square.describe()
