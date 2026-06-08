#include <iostream>
#include <string>

int main() {
    char c1 = 'A';                     // ASCII-символ
    char c2 = '\n';                    // Управляющий символ
    char c3 = 0x41;                    // То же, что 'A'

    const char* ascii_str = "Hello";
    const char* utf8_str = u8"Привет"; // UTF-8 строка (C++11+)

    std::cout << "c1 = " << c1 << '\n';
    std::cout << "ASCII: " << ascii_str << '\n';
    std::cout << "UTF-8: " << utf8_str << '\n';

    // char может хранить байты любого происхождения
    unsigned char buffer[] = {0xDE, 0xAD, 0xBE, 0xEF};
    for (auto b : buffer) {
        std::cout << std::hex << static_cast<int>(b) << ' ';
    }
    std::cout << '\n';

    return 0;
}
