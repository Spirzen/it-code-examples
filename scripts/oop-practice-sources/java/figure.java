// 1. Создаем чертеж (класс) для любой фигуры
class Figure {
    String name;
    String color;

    Figure(String name, String color) {
        this.name = name;
        this.color = color;
    }

    void describe() {
        System.out.println("Я " + color + " " + name);
    }
}

public class Main {
    public static void main(String[] args) {
        // 2. Создаем конкретные фигуры (объекты)
        Figure circle = new Figure("Круг", "Красный");
        Figure square = new Figure("Квадрат", "Синий");

        // 3. Используем их
        circle.describe();   // Я Красный Круг
        square.describe();   // Я Синий Квадрат
    }
}
