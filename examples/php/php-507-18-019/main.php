<?php

class Car
{
    public const SERVICE_INTERVAL = 15000;
    public const FUEL_PER_KM = 0.1;

    public function __construct(
        public string $brand,
        public float $fuel = 40.0,
        public int $mileage = 0
    ) {}

    public function refuel(float $liters): void
    {
        $this->fuel += $liters;
        echo sprintf("Заправка: +%.0f л. Топливо: %.1f л\n", $liters, $this->fuel);
    }

    public function drive(int $km): void
    {
        $needed = $km * self::FUEL_PER_KM;
        if ($needed > $this->fuel) {
            echo "Ошибка: недостаточно топлива\n";
            return;
        }
        $this->fuel -= $needed;
        $this->mileage += $km;
        echo sprintf(
            "Проехали %d км. Топливо: %.1f л. Пробег: %d км\n",
            $km,
            $this->fuel,
            $this->mileage
        );
        if ($this->mileage >= self::SERVICE_INTERVAL) {
            echo "⚠️ ВНИМАНИЕ: требуется техобслуживание!\n";
        }
    }
}

$car = new Car('Lada');
$car->refuel(10);
$car->drive(5000);
$car->drive(11000);
