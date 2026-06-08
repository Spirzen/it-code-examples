#include <iostream>
#include <type_traits>

void handleChar(char c) {
    std::cout << "char: " << static_cast<int>(c) << '\n';
}

void handleSignedChar(signed char c) {
    std::cout << "signed char: " << static_cast<int>(c) << '\n';
}

void handleUnsignedChar(unsigned char c) {
    std::cout << "unsigned char: " << static_cast<int>(c) << '\n';
}

int main() {
    // Эти три вызова могут вести к разным перегрузкам!
    char a = -1;
    signed char b = -1;
    unsigned char c = 255; // эквивалентно -1 в signed, но не в unsigned

    handleChar(a);          // вызывает handleChar
    handleSignedChar(b);    // вызывает handleSignedChar
    handleUnsignedChar(c);  // вызывает handleUnsignedChar

    // Проверка различий на уровне типов
    std::cout << "\nТипы различны:\n";
    std::cout << "char == signed char?   " << std::is_same_v<char, signed char> << '\n';
    std::cout << "char == unsigned char? " << std::is_same_v<char, unsigned char> << '\n';

    return 0;
}
