#include <iostream>
#include <string>
#include <algorithm>

class Smartphone {
private:
    std::string model;
    int battery;

public:
    explicit Smartphone(const std::string& model) : model(model), battery(20) {}

    void call() {
        battery = std::max(0, battery - 5);
        std::cout << "Звонок с " << model << "... Заряд: " << battery << "%" << std::endl;
    }

    void charge() {
        battery = std::min(100, battery + 30);
        std::cout << "Зарядка " << model << "... Заряд: " << battery << "%" << std::endl;
    }

    void show_status() const {
        std::cout << "Смартфон " << model << ": заряд " << battery << "%" << std::endl;
    }
};

int main() {
    Smartphone phone("Pixel");
    phone.show_status();
    phone.call();
    phone.charge();
    phone.show_status();
    return 0;
}
