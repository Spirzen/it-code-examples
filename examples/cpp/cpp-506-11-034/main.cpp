#include <iostream>

int main() {
    // Объявление и инициализация массива из 5 целых чисел
    int numbers[5] = {10, 20, 30, 40, 50};

    // Доступ к элементам по индексу
    std::cout << "Первый элемент: " << numbers[0] << std::endl; // 10
    std::cout << "Третий элемент: " << numbers[2] << std::endl; // 30

    // Изменение значения элемента
    numbers[1] = 25;
    std::cout << "Изменённый второй элемент: " << numbers[1] << std::endl; // 25

    // Перебор всех элементов
    for (int i = 0; i < 5; ++i) {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
