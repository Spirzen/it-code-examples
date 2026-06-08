#include <type_traits>
#include <iostream>

// Шаблонная функция, которая может возвращать что угодно — или ничего
template<typename T>
T getValue();

// Специализация для void: функция просто завершается
template<>
void getValue<void>() {
    std::cout << "Специализация для void: ничего не возвращаем\n";
}

// Пример использования в условной логике
template<typename Func>
auto callAndReport(Func f) -> decltype(f()) {
    std::cout << "Вызываем функцию с возвратом...\n";
    return f();
}

template<typename Func>
void callAndReport(Func f, std::void_t<decltype(f())>* = nullptr) {
    // Перегрузка для случая, когда f() возвращает void
    std::cout << "Вызываем функцию без возврата...\n";
    f();
}

void sayHello() {
    std::cout << "Привет!\n";
}

int getNumber() {
    return 123;
}

int main() {
    getValue<void>();        // вызывает специализацию
    getValue<int>();         // ошибка линковки, но демонстрирует идею

    callAndReport(sayHello);   // выбирает перегрузку для void
    callAndReport(getNumber);  // выбирает перегрузку с возвратом

    return 0;
}
