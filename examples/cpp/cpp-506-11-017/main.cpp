#include <iostream>
#include <cmath>

bool nearlyEqual(double a, double b, double epsilon = 1e-9) {
    return std::abs(a - b) < epsilon;
}

int main() {
    double x = 0.1 + 0.2;
    double y = 0.3;

    std::cout << "x = " << x << '\n';
    std::cout << "y = " << y << '\n';
    std::cout << "x == y? " << (x == y ? "да" : "нет") << '\n';
    std::cout << "nearlyEqual(x, y)? " << (nearlyEqual(x, y) ? "да" : "нет") << '\n';

    // Для больших чисел нужен относительный эпсилон
    double a = 1e10;
    double b = a + 1.0;
    std::cout << "\nБольшие числа:\n";
    std::cout << "a = " << a << ", b = " << b << '\n';
    std::cout << "Абсолютное сравнение: " << (nearlyEqual(a, b) ? "равны" : "не равны") << '\n';

    // Относительное сравнение
    bool relEqual = std::abs(a - b) <= 1e-9 * std::max(std::abs(a), std::abs(b));
    std::cout << "Относительное сравнение: " << (relEqual ? "равны" : "не равны") << '\n';

    return 0;
}
