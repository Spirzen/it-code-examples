#include <iostream>
#include <cstring> // для strlen, strcpy и других функций

int main() {
    // Объявление и инициализация C-style строки
    char greeting[] = "Привет";

    // Вывод строки
    std::cout << greeting << std::endl;

    // Длина строки
    std::cout << "Длина: " << strlen(greeting) << std::endl;

    // Копирование строки
    char copy[20];
    strcpy(copy, greeting);
    std::cout << "Копия: " << copy << std::endl;

    // Конкатенация
    char message[50] = "Сообщение: ";
    strcat(message, greeting);
    std::cout << message << std::endl;

    return 0;
}
