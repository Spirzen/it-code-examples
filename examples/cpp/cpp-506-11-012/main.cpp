#include <iostream>
#include <climits>

int main() {
    // Беззнаковое переполнение — определено стандартом
    unsigned int max_ui = UINT_MAX;
    unsigned int wrapped = max_ui + 1;
    std::cout << "UINT_MAX + 1 = " << wrapped << " (ожидаемо 0)\n";

    // Знаковое переполнение — неопределённое поведение!
    // Следующий код формально некорректен:
    int max_i = INT_MAX;
    int overflowed = max_i + 1; // Не делайте так!

    // На практике компилятор может оптимизировать, исходя из предположения,
    // что такого не произойдёт. Результат непредсказуем.
    std::cout << "INT_MAX + 1 = " << overflowed << " (поведение не определено!)\n";

    return 0;
}
