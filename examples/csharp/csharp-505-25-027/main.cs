class Car
{
    public const int ServiceInterval = 15000;
    public const double FuelPerKm = 0.1;
    public string Brand { get; }
    public double Fuel { get; private set; }
    public int Mileage { get; private set; }

    public Car(string brand)
    {
        Brand = brand;
        Fuel = 40.0;
        Mileage = 0;
    }

    public void Refuel(double liters)
    {
        Fuel += liters;
        Console.WriteLine($"Заправка: +{liters} л. Топливо: {Fuel:F1} л");
    }

    public void Drive(int km)
    {
        var needed = km * FuelPerKm;
        if (needed > Fuel)
        {
            Console.WriteLine("Ошибка: недостаточно топлива");
            return;
        }
        Fuel -= needed;
        Mileage += km;
        Console.WriteLine($"Проехали {km} км. Топливо: {Fuel:F1} л. Пробег: {Mileage} км");
        if (Mileage >= ServiceInterval)
        {
            Console.WriteLine("⚠️ ВНИМАНИЕ: требуется техобслуживание!");
        }
    }
}

class Program
{
    static void Main()
    {
        var car = new Car("Lada");
        car.Refuel(10);
        car.Drive(5000);
        car.Drive(11000);
    }
}
