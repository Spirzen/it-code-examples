#include <iostream>

enum Color {
    RED,
    GREEN,
    BLUE
};

int main() {
    Color background = GREEN;
    std::cout << "Цвет: " << background << std::endl; // 1

    if (background == GREEN) {
        std::cout << "Фон зелёный." << std::endl;
    }

    return 0;
}
