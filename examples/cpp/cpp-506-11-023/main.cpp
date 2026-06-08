#include <iostream>
#include <cstdint>

int main() {
    int number = 42;
    double pi = 3.14159;
    char text[] = "Hello";

    // void* может указывать на любой объект
    void* ptr1 = &number;
    void* ptr2 = &pi;
    void* ptr3 = text; // массив превращается в указатель

    // Но из void* нельзя напрямую прочитать значение — нужен явный каст
    std::cout << "number через void*: " << *static_cast<int*>(ptr1) << '\n';
    std::cout << "pi через void*:     " << *static_cast<double*>(ptr2) << '\n';
    std::cout << "text через void*:   " << static_cast<char*>(ptr3) << '\n';

    // void* нельзя разыменовать напрямую:
    // std::cout << *ptr1; // Ошибка компиляции!

    // void* не может указывать на функцию (без reinterpret_cast)
    // void (*f)() = nullptr;
    // void* p = f; // Ошибка! Нестандартное преобразование

    return 0;
}
