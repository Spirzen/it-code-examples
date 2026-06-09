#include <iostream>
#include <string>
#include <iomanip>

class Car {
public:
    static const int SERVICE_INTERVAL = 15000;
    static constexpr double FUEL_PER_KM = 0.1;
    std::string brand;
    double fuel;
    int mileage;

    explicit Car(const std::string& brand) : brand(brand), fuel(40.0), mileage(0) {}

    void refuel(double liters) {
        fuel += liters;
        std::cout << std::fixed << std::setprecision(1);
        std::cout << "Заправка: +" << liters << " л. Топливо: " << fuel << " л" << std::endl;
    }

    void drive(int km) {
        double needed = km * FUEL_PER_KM;
        if (needed > fuel) {
            std::cout << "Ошибка: недостаточно топлива" << std::endl;
            return;
        }
        fuel -= needed;
        mileage += km;
        std::cout << std::fixed << std::setprecision(1);
        std::cout << "Проехали " << km << " км. Топливо: " << fuel << " л. Пробег: " << mileage << " км" << std::endl;
        if (mileage >= SERVICE_INTERVAL) {
            std::cout << "⚠️ ВНИМАНИЕ: требуется техобслуживание!" << std::endl;
        }
    }
};

int main() {
    Car car("Lada");
    car.refuel(10);
    car.drive(5000);
    car.drive(11000);
    return 0;
}
