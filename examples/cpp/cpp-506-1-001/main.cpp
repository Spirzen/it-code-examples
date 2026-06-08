#include <iostream>
#include <string>
#include <memory>

class Greeting {
    std::string message;
public:
    explicit Greeting(std::string msg) : message(std::move(msg)) {}
    void print() const { std::cout << message << '\n'; }
};

int main() {
    auto hello = std::make_unique<Greeting>("Hello, C++!");
    hello->print();
    return 0;
}
