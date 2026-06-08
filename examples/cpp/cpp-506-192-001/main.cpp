#include <stdexcept>
#include <iostream>

double divide(double a, double b) {
    if (b == 0.0)
        throw std::invalid_argument("division by zero");
    return a / b;
}

int main() {
    try {
        std::cout << divide(10, 0) << '\n';
    } catch (const std::invalid_argument& ex) {
        std::cerr << "Logic error: " << ex.what() << '\n';
    } catch (const std::exception& ex) {
        std::cerr << "Other std error: " << ex.what() << '\n';
    } catch (...) {
        std::cerr << "Unknown exception\n";
    }
    return 0;
}
