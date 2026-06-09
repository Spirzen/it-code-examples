class Car {
    static final int SERVICE_INTERVAL = 15000;
    static final double FUEL_PER_KM = 0.1;
    String brand;
    double fuel;
    int mileage;

    Car(String brand) {
        this.brand = brand;
        this.fuel = 40.0;
        this.mileage = 0;
    }

    void refuel(double liters) {
        fuel += liters;
        System.out.printf("Заправка: +%.0f л. Топливо: %.1f л%n", liters, fuel);
    }

    void drive(int km) {
        double needed = km * FUEL_PER_KM;
        if (needed > fuel) {
            System.out.println("Ошибка: недостаточно топлива");
            return;
        }
        fuel -= needed;
        mileage += km;
        System.out.printf("Проехали %d км. Топливо: %.1f л. Пробег: %d км%n", km, fuel, mileage);
        if (mileage >= SERVICE_INTERVAL) {
            System.out.println("⚠️ ВНИМАНИЕ: требуется техобслуживание!");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Car car = new Car("Lada");
        car.refuel(10);
        car.drive(5000);
        car.drive(11000);
    }
}
