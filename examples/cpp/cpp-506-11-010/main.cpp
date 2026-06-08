#include <iostream>
#include <climits>

int main() {
    std::cout << "sizeof(short)      = " << sizeof(short)      << " bytes (" << CHAR_BIT * sizeof(short)      << " bits)\n";
    std::cout << "sizeof(int)        = " << sizeof(int)        << " bytes (" << CHAR_BIT * sizeof(int)        << " bits)\n";
    std::cout << "sizeof(long)       = " << sizeof(long)       << " bytes (" << CHAR_BIT * sizeof(long)       << " bits)\n";
    std::cout << "sizeof(long long)  = " << sizeof(long long)  << " bytes (" << CHAR_BIT * sizeof(long long)  << " bits)\n";

    // Минимальные гарантии стандарта:
    std::cout << "\nГарантированный минимум:\n";
    std::cout << "short:   >= 16 bits\n";
    std::cout << "int:     >= 16 bits (но обычно 32)\n";
    std::cout << "long:    >= 32 bits\n";
    std::cout << "long long: >= 64 bits\n";

    return 0;
}
