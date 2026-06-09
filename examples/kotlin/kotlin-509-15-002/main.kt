open class Figure(val name: String, val color: String) {
    fun describe() {
        println("Фигура «$name», цвет: $color")
    }
}

class Circle(color: String) : Figure("Круг", color)

class Square(color: String) : Figure("Квадрат", color)

fun main() {
    val circle = Circle("красный")
    val square = Square("синий")
    circle.describe()
    square.describe()
}
