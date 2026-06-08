#include <vector>
#include <cmath>

// Используем float для экономии памяти в больших массивах
void processLargeDataset() {
    const size_t N = 10'000'000;
    std::vector<float> data(N); // 40 МБ вместо 80 МБ при double

    for (size_t i = 0; i < N; ++i) {
        data[i] = std::sin(static_cast<float>(i) * 0.001f);
    }
    // Подходит для графики, ML, обработки сигналов
}

// Используем double для высокой точности
double computeFinancialValue(double principal, double rate, int years) {
    return principal * std::pow(1.0 + rate, years);
    // Финансы, научные расчёты — требуют double
}

int main() {
    processLargeDataset();
    double result = computeFinancialValue(1000.0, 0.05, 10);
    std::cout << "Итоговая сумма: " << result << '\n';
    return 0;
}
