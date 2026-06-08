#include <iostream>

int main() {
    char letter = 'A';
    char digit = '7';
    char symbol = '@';

    std::cout << "Буква: " << letter << std::endl;   // Вывод: A
    std::cout << "Цифра: " << digit << std::endl;    // Вывод: 7
    std::cout << "Символ: " << symbol << std::endl;  // Вывод: @

    // Символ можно использовать в арифметике
    char nextLetter = letter + 1; // 'B'
    std::cout << "Следующая буква: " << nextLetter << std::endl;

    return 0;
}
