#include <functional>

std::function<int(int, int)> op;

op = add;
std::cout << op(1, 2); // 3

op = [](int a, int b) { return a * b; };
std::cout << op(3, 4); // 12

struct Multiplier {
    int factor;
    int operator()(int x, int y) const { return (x + y) * factor; }
};
op = Multiplier{10};
std::cout << op(1, 2); // 30
