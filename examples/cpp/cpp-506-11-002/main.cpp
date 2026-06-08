#include <iostream>

int main() {
    int x = 5;
    int y = 0;
    double z = -3.14;
    char c = '\0';

    bool b1 = x;  // true (ненулевое значение)
    bool b2 = y;  // false (нулевое значение)
    bool b3 = z;  // true (ненулевое значение)
    bool b4 = c;  // false (нулевой символ)

    std::cout << "b1: " << b1 << '\n';  // 1
    std::cout << "b2: " << b2 << '\n';  // 0
    std::cout << "b3: " << b3 << '\n';  // 1
    std::cout << "b4: " << b4 << '\n';  // 0

    return 0;
}
