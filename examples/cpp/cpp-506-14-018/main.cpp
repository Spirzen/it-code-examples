// Плохо: ручной цикл
int sum = 0;
for (int x : v) {
    if (x > 0) sum += x;
}

// Лучше: алгоритмы
auto positive = [](int x) { return x > 0; };
int sum = std::accumulate(
    std::begin(v), std::end(v), 0,
    [&](int acc, int x) { return acc + (positive(x) ? x : 0); }
);

// Или: сначала фильтрация (C++20 ranges)
#include <ranges>
auto sum = v | std::views::filter(positive)
             | std::views::transform([](int x) { return x; })
             | std::ranges::accumulate(0);
