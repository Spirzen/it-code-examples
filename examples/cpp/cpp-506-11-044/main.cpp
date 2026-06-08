#include <chrono>

// 5_min → std::chrono::minutes{5}
constexpr std::chrono::minutes operator"" _min(unsigned long long m) {
    return std::chrono::minutes{m};
}

// 3.5_s → std::chrono::duration<long double, std::ratio<1>>{3.5}
constexpr auto operator"" _s(long double s) {
    return std::chrono::duration<long double>{s};
}

// 100_km → целое количество метров (для вычислений без плавающей точки)
constexpr long long operator"" _km(unsigned long long km) {
    return km * 1000;
}

// Использование:
auto delay = 2_min + 0.5_s;               // std::chrono::duration<double>
auto distance = 5_km + 300;               // 5300 (метров)
auto flight_time = distance / 250.0;      // без единиц — ошибка дизайна!
