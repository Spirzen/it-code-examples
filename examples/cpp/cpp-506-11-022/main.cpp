#include <iostream>

// Функция ничего не возвращает — тип void
void logMessage(const char* msg) {
    std::cout << "[LOG] " << msg << '\n';
}

// Такая функция не может вернуть значение
// return 42; // Ошибка компиляции!

int main() {
    logMessage("Программа запущена");
    logMessage("Завершение работы");
    return 0;
}
