#include <iostream>

int main() {
    char c = 'X';
    wchar_t wc = static_cast<wchar_t>(c);       // Расширение до широкого символа
    char16_t c16 = static_cast<char16_t>(c);
    char32_t c32 = static_cast<char32_t>(c);

    std::cout << "Original: " << c << '\n';
    std::cout << "As wchar_t: " << static_cast<int>(wc) << '\n';
    std::cout << "As char16_t: " << static_cast<uint16_t>(c16) << '\n';
    std::cout << "As char32_t: " << static_cast<uint32_t>(c32) << '\n';

    return 0;
}
