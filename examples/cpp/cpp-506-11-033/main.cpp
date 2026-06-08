#include <iostream>

int main() {
    int original = 10;
    int& ref = original; // ref — это другое имя для original

    std::cout << "Оригинал: " << original << std::endl; // 10
    std::cout << "Через ссылку: " << ref << std::endl;  // 10

    ref = 20; // изменяем значение через ссылку
    std::cout << "После изменения: " << original << std::endl; // 20

    return 0;
}
