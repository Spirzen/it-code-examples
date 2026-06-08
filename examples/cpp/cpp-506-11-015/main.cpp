#include <iostream>
#include <iomanip> // для управления точностью вывода

int main() {
    float price = 19.99f;
    double pi = 3.141592653589793;
    long double preciseValue = 1.234567890123456789L;

    // Установка точности вывода
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Цена: " << price << " руб." << std::endl;

    std::cout << std::setprecision(10);
    std::cout << "Число Пи: " << pi << std::endl;

    std::cout << std::setprecision(15);
    std::cout << "Точное значение: " << preciseValue << std::endl;

    return 0;
}
