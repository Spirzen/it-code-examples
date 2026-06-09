<?php

class Animal
{
    public function __construct(protected string $name) {}

    public function eat(): void
    {
        echo "{$this->name} ест\n";
    }
}

class Cat extends Animal
{
    public function speak(): void
    {
        echo "Мяу!\n";
    }
}

class Dog extends Animal
{
    public function speak(): void
    {
        echo "Гав!\n";
    }
}

$cat = new Cat('Мурка');
$dog = new Dog('Шарик');
$cat->eat();
$cat->speak();
$dog->eat();
$dog->speak();
