#include <iostream>
#include <vector>

int sum(const std::vector<int>& values) {
    int total = 0;
    for (int v : values) {
        total += v;
    }
    return total;
}

int main() {
    std::vector<int> data{1, 2, 3, 5, 8};
    std::cout << "sum=" << sum(data) << '\n';
}
