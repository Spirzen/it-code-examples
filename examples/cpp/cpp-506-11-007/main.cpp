#include <iostream>
#include <string>

int main() {
    char16_t c16 = u'λ';               // UTF-16 символ
    char32_t c32 = U'🙂';              // UTF-32 символ (эмодзи)

    std::u16string str16 = u"Привет 🌍";
    std::u32string str32 = U"Здравствуй, Вселенная! 🚀";

    // Прямой вывод в std::cout невозможен — нет стандартного оператора <<
    // Но можно вывести числовые значения:

    std::cout << "char16_t value: 0x" << std::hex << static_cast<uint16_t>(c16) << '\n';
    std::cout << "char32_t value: 0x" << std::hex << static_cast<uint32_t>(c32) << '\n';

    // Или длины строк:
    std::cout << "u16string length: " << str16.size() << " code units\n";
    std::cout << "u32string length: " << str32.size() << " code points\n";

    return 0;
}
