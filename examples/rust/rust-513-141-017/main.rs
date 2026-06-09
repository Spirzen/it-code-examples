struct Car {
    brand: String,
    fuel: f64,
    mileage: i32,
}

impl Car {
    const SERVICE_INTERVAL: i32 = 15000;
    const FUEL_PER_KM: f64 = 0.1;

    fn new(brand: &str) -> Self {
        Self {
            brand: brand.to_string(),
            fuel: 40.0,
            mileage: 0,
        }
    }

    fn refuel(&mut self, liters: f64) {
        self.fuel += liters;
        println!("Заправка: +{:.0} л. Топливо: {:.1} л", liters, self.fuel);
    }

    fn drive(&mut self, km: i32) {
        let needed = km as f64 * Self::FUEL_PER_KM;
        if needed > self.fuel {
            println!("Ошибка: недостаточно топлива");
            return;
        }
        self.fuel -= needed;
        self.mileage += km;
        println!(
            "Проехали {} км. Топливо: {:.1} л. Пробег: {} км",
            km, self.fuel, self.mileage
        );
        if self.mileage >= Self::SERVICE_INTERVAL {
            println!("⚠️ ВНИМАНИЕ: требуется техобслуживание!");
        }
    }
}

fn main() {
    let mut car = Car::new("Lada");
    car.refuel(10.0);
    car.drive(5000);
    car.drive(11000);
}
