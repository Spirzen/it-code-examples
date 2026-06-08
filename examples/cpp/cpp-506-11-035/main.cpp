#include <iostream>

int main() {
    // Двумерный массив 2×3
    int matrix[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };

    // Доступ к элементу во второй строке, третьем столбце
    std::cout << "Элемент [1][2]: " << matrix[1][2] << std::endl; // 6

    // Вывод всей матрицы
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 3; ++j) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
