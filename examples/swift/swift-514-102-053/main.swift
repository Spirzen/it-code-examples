class Car {
    static let serviceInterval = 15000
    static let fuelPerKm = 0.1
    let brand: String
    var fuel: Double
    var mileage: Int

    init(brand: String) {
        self.brand = brand
        self.fuel = 40.0
        self.mileage = 0
    }

    func refuel(_ liters: Double) {
        fuel += liters
        print(String(format: "Заправка: +%.0f л. Топливо: %.1f л", liters, fuel))
    }

    func drive(_ km: Int) {
        let needed = Double(km) * Self.fuelPerKm
        if needed > fuel {
            print("Ошибка: недостаточно топлива")
            return
        }
        fuel -= needed
        mileage += km
        print(String(format: "Проехали %d км. Топливо: %.1f л. Пробег: %d км", km, fuel, mileage))
        if mileage >= Self.serviceInterval {
            print("⚠️ ВНИМАНИЕ: требуется техобслуживание!")
        }
    }
}

let car = Car(brand: "Lada")
car.refuel(10)
car.drive(5000)
car.drive(11000)
