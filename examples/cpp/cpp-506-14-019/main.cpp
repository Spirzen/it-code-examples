#include <iostream>
#include <string>
#include <algorithm>

class Figure {
public:
    std::string name;
    std::string color;

    Figure(const std::string& name, const std::string& color)
        : name(name), color(color) {}

    void describe() const {
        std::cout << "Фигура «" << name << "», цвет: " << color << std::endl;
    }
};

class Circle : public Figure {
public:
    explicit Circle(const std::string& color) : Figure("Круг", color) {}
};

class Square : public Figure {
public:
    explicit Square(const std::string& color) : Figure("Квадрат", color) {}
};

int main() {
    Circle circle("красный");
    Square square("синий");
    circle.describe();
    square.describe();
    return 0;
}
