#include <iostream>

int main() {
    short smallNumber = 32767;
    int usualNumber = 1000000;
    long bigNumber = 2147483647L;
    long long hugeNumber = 9223372036854775807LL;

    std::cout << "short: " << smallNumber << std::endl;
    std::cout << "int: " << usualNumber << std::endl;
    std::cout << "long: " << bigNumber << std::endl;
    std::cout << "long long: " << hugeNumber << std::endl;

    // Отрицательные значения также допустимы
    int negative = -42;
    std::cout << "Отрицательное число: " << negative << std::endl;

    return 0;
}
