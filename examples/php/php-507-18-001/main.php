<?php

class Unit {
    public $name = "Имя";
    public $intel = 10;
    public $agility = 10;
    public $strength = 10;
    public $health = 100;
    public $mana = 50;
    public $level = 1;

    public function getDamage() {
        return ($this->intel + $this->agility + $this->strength) + ($this->level * 2);
    }

    public function attack($target) {
        echo $this->name . " атакует " . $target->name . " и наносит " . $this->getDamage() . " единиц урона." . PHP_EOL;
        $target->health -= $this->getDamage();
        echo $target->name . " теперь имеет " . $target->health . " здоровья." . PHP_EOL;
    }
}

$warrior = new Unit();
$warrior->name = "Воин";
$warrior->intel = 5;
$warrior->agility = 15;
$warrior->strength = 30;

$mage = new Unit();
$mage->name = "Маг";
$mage->intel = 35;
$mage->agility = 10;
$mage->strength = 5;

$warrior->attack($mage);
$mage->attack($warrior);

?>
