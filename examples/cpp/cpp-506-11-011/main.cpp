#include <iostream>
#include <cstdint>

int main() {
    signed int si = -42;
    unsigned int ui = 4294967254U; // большое положительное число

    std::cout << "signed int:   " << si << '\n';
    std::cout << "unsigned int: " << ui << '\n';

    // Беззнаковый тип не может быть отрицательным:
    unsigned int u = -1; // Не ошибка! Результат — максимальное значение типа
    std::cout << "unsigned int u = -1 → " << u << '\n'; // Выведет 4294967295 на 32-битной системе

    return 0;
}
