#include <iostream>

// Пример: регистр аппаратного устройства (гипотетический)
volatile int* hardware_register = reinterpret_cast<volatile int*>(0x12345678);

void waitForSignal() {
    // Без volatile компилятор мог бы оптимизировать цикл в бесконечный,
    // считая, что значение не меняется
    while (*hardware_register == 0) {
        // ждём, пока регистр не станет ненулевым
    }
    std::cout << "Сигнал получен!\n";
}

// Пример с обычной переменной (не рекомендуется без причины)
volatile int flag = 0;

void simulateExternalChange() {
    // Представим, что другой поток или прерывание меняет flag
    // (в реальности для потоков нужно std::atomic!)
    flag = 1;
}

int main() {
    // В реальном коде volatile используется редко:
    // - в embedded-системах
    // - при взаимодействии с hardware
    // - в signal handlers (ограниченно)

    // Для многопоточности volatile НЕ подходит!
    simulateExternalChange();
    if (flag) {
        std::cout << "Флаг установлен\n";
    }

    return 0;
}
