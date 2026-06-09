<?php

class Figure
{
    public function __construct(
        private string $name,
        private string $color
    ) {}

    public function describe(): void
    {
        echo "Фигура «{$this->name}», цвет: {$this->color}\n";
    }
}

class Circle extends Figure
{
    public function __construct(string $color)
    {
        parent::__construct('Круг', $color);
    }
}

class Square extends Figure
{
    public function __construct(string $color)
    {
        parent::__construct('Квадрат', $color);
    }
}

$circle = new Circle('красный');
$square = new Square('синий');
$circle->describe();
$square->describe();
