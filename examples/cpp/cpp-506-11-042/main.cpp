#include <iostream>
#include <string>

int main() {
    // Объявление и инициализация
    std::string text = "Здравствуйте";
    std::string name("Мир");

    // Вывод
    std::cout << text << ", " << name << "!" << std::endl;

    // Длина строки
    std::cout << "Длина: " << text.length() << std::endl;

    // Конкатенация
    std::string full = text + ", " + name + "!";
    std::cout << full << std::endl;

    // Доступ к символу по индексу
    std::cout << "Первый символ: " << text[0] << std::endl;

    // Изменение символа
    text[0] = 'з'; // теперь "здравствуйте" (строчная буква)
    std::cout << text << std::endl;

    // Поиск подстроки
    size_t pos = full.find("Мир");
    if (pos != std::string::npos) {
        std::cout << "Найдено на позиции: " << pos << std::endl;
    }

    return 0;
}
