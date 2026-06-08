#include <iostream>
#include <cmath>
#include <limits>

int main() {
    double inf = std::numeric_limits<double>::infinity();
    double nan = std::numeric_limits<double>::quiet_NaN();

    std::cout << "inf = " << inf << '\n';
    std::cout << "nan = " << nan << '\n';

    // Арифметика с бесконечностью
    std::cout << "inf + 1 = " << inf + 1 << '\n';
    std::cout << "inf * -1 = " << inf * -1 << '\n';
    std::cout << "inf - inf = " << inf - inf << " (получаем NaN)\n";

    // Проверка на NaN
    std::cout << "isnan(nan) = " << std::isnan(nan) << '\n';
    std::cout << "isnan(inf) = " << std::isnan(inf) << '\n';

    // Важно: NaN != NaN всегда!
    std::cout << "nan == nan → " << (nan == nan ? "true" : "false") << '\n';
    std::cout << "isnan(nan) — правильный способ проверки\n";

    // Деление на ноль
    double zero = 0.0;
    std::cout << "1.0 / 0.0 = " << 1.0 / zero << '\n';
    std::cout << "-1.0 / 0.0 = " << -1.0 / zero << '\n';

    return 0;
}
