#include <fstream>

void inner() {
    std::ifstream file("missing.txt");
    throw std::runtime_error("fail");
}

void outer() {
    try {
        inner();
    } catch (const std::exception& e) {
        std::cerr << e.what() << '\n';
    }
}
