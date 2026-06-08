#include <iostream>

int main() {
    char greeting[] = "Привет"; // автоматически добавляется завершающий нуль '\0'

    std::cout << greeting << std::endl; // Вывод: Привет

    // Ручной перебор до нулевого символа
    for (int i = 0; greeting[i] != '\0'; ++i) {
        std::cout << greeting[i] << "-";
    }
    std::cout << std::endl;

    return 0;
}
