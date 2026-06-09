<?php

class Smartphone
{
    public function __construct(
        private string $model,
        private int $battery = 20
    ) {}

    public function call(): void
    {
        $this->battery = max(0, $this->battery - 5);
        echo "Звонок с {$this->model}... Заряд: {$this->battery}%\n";
    }

    public function charge(): void
    {
        $this->battery = min(100, $this->battery + 30);
        echo "Зарядка {$this->model}... Заряд: {$this->battery}%\n";
    }

    public function showStatus(): void
    {
        echo "Смартфон {$this->model}: заряд {$this->battery}%\n";
    }
}

$phone = new Smartphone('Pixel');
$phone->showStatus();
$phone->call();
$phone->charge();
$phone->showStatus();
