| warrior mage |
warrior := Fighter new.
warrior
    name: 'Воин';
    intel: 5;
    agility: 15;
    strength: 30.

mage := Fighter new.
mage
    name: 'Маг';
    intel: 35;
    agility: 10;
    strength: 5.

warrior attack: mage.
mage attack: warrior.
