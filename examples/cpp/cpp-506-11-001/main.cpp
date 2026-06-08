#include <iostream>

int main() {
    bool isReady = true;
    bool isError = false;

    std::cout << "isReady: " << isReady << '\n';   // Выведет: 1
    std::cout << "isError: " << isError << '\n';   // Выведет: 0

    if (isReady) {
        std::cout << "Система готова к работе." << std::endl;
    }

    return 0;
}
