#include <iostream>
#include <iomanip>

int main() {
    double a = 1e20;
    double b = -1e20;
    double c = 1.0;

    double left_to_right = (a + b) + c;   // (1e20 - 1e20) + 1 = 0 + 1 = 1
    double right_to_left = a + (b + c);   // 1e20 + (-1e20 + 1) = 1e20 + (-1e20) = 0

    std::cout << std::setprecision(17);
    std::cout << "(a + b) + c = " << left_to_right << '\n';
    std::cout << "a + (b + c) = " << right_to_left << '\n';
    std::cout << "Равны? " << (left_to_right == right_to_left ? "да" : "нет") << '\n';

    return 0;
}
