#include <iostream>
#include <iomanip>

int main() {
    float f = 0.1f;
    double d = 0.1;

    std::cout << std::setprecision(17);
    std::cout << "float  0.1 ≈ " << f << '\n';
    std::cout << "double 0.1 ≈ " << d << '\n';

    // Сумма 0.1 десять раз не даёт ровно 1.0
    double sum = 0.0;
    for (int i = 0; i < 10; ++i) {
        sum += 0.1;
    }

    std::cout << "Сумма десяти 0.1 = " << sum << '\n';
    std::cout << "Равно ли 1.0? " << (sum == 1.0 ? "да" : "нет") << '\n';

    return 0;
}
