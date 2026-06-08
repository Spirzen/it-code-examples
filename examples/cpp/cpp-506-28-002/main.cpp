#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};

    // Сортировка работает одинаково для вектора
    std::sort(numbers.begin(), numbers.end());

    // Вычисление суммы через алгоритм accumulate
    int sum = std::accumulate(numbers.begin(), numbers.end(), 0);

    // Преобразование элементов: возведение в квадрат
    std::transform(numbers.begin(), numbers.end(), numbers.begin(),
                   [](int x) { return x * x; });

    std::cout << "Сумма исходных чисел: " << sum << "\n";
    std::cout << "Квадраты чисел: ";
    for (int n : numbers) {
        std::cout << n << " ";
    }
    std::cout << "\n";

    return 0;
}
