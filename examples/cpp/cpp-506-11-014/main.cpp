#include <vector>
#include <cstdint>

// Пример 1: индексация контейнеров — используем size_t или int
void processVector(const std::vector<double>& vec) {
    for (int i = 0; i < static_cast<int>(vec.size()); ++i) {
        // Допустимо, если размер вектора умеренный
    }
}

// Пример 2: работа с бинарным протоколом — нужен точный размер
struct NetworkHeader {
    std::uint32_t magic;      // 4 байта
    std::uint16_t version;    // 2 байта
    std::uint16_t payload_len; // 2 байта
};

// Пример 3: математические вычисления — часто достаточно int
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    auto header = NetworkHeader{0xDEADBEEF, 1, 1024};
    std::cout << "Magic: 0x" << std::hex << header.magic << '\n';
    std::cout << "Factorial(5): " << std::dec << factorial(5) << '\n';
    return 0;
}
