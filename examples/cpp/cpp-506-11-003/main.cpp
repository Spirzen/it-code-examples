#include <iostream>
#include <vector>

int main() {
    int value = 42;
    int* ptr = nullptr;
    std::vector<int> emptyVec;
    std::vector<int> filledVec = {1, 2, 3};

    if (value) {
        std::cout << "value is truthy\n";  // выполнится
    }

    if (!ptr) {
        std::cout << "ptr is null\n";      // выполнится
    }

    if (emptyVec.empty()) {
        std::cout << "vector is empty\n";  // предпочтительный способ проверки
    }

    if (filledVec.size()) {
        std::cout << "vector has elements (но лучше использовать !vec.empty())\n";
    }

    return 0;
}
