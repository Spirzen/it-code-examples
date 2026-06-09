class Car:
    def __init__(self, brand, year, mileage=0):
        self.brand = brand
        self.year = year
        self.mileage = mileage  # Пробег в км
        self.fuel = 0           # Топливо в литрах

    def refuel(self, liters):
        if liters > 0:
            self.fuel += liters
            print(f"Залито {liters}л. Теперь в баке {self.fuel}л")

    def drive(self, km):
        consumption = km * 0.1  # Расход 10л на 100км -> 0.1л на 1км
        if self.fuel < consumption:
            print(f"Не хватает топлива! Нужно {consumption:.1f}л, в баке {self.fuel}л")
            return

        self.fuel -= consumption
        self.mileage += km
        print(f"Проехали {km}км. Пробег: {self.mileage}км, осталось топлива: {self.fuel:.1f}л")

        # Проверка на ТО
        if self.mileage >= 15000:
            print("⚠️ ВНИМАНИЕ: Пора проходить техническое обслуживание!")

    def service_required(self):
        return self.mileage >= 15000


# Тест-драйв
my_car = Car("Toyota Camry", 2022, 14500)
my_car.refuel(50)
my_car.drive(600)   # Проехали 600км. Пробег: 15100км
# ⚠️ ВНИМАНИЕ: Пора проходить техническое обслуживание!

if my_car.service_required():
    print("Запишитесь на ТО!")
