#include <iostream>

int main() {
    int value = 42;
    int* ptr = &value; // ptr содержит адрес переменной value

    std::cout << "Значение: " << value << std::endl;        // 42
    std::cout << "Адрес: " << ptr << std::endl;             // например, 0x7fff5fbff6ac
    std::cout << "Значение через указатель: " << *ptr << std::endl; // 42

    *ptr = 100; // изменяем значение через указатель
    std::cout << "Новое значение: " << value << std::endl;  // 100

    return 0;
}
