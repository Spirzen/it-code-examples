package main

import "fmt"

type Unit struct {
	name     string
	intel    int
	agility  int
	strength int
	health   int
	mana     int
	level    int
}

func NewUnit() *Unit {
	return &Unit{
		name:     "Имя",
		intel:    10,
		agility:  10,
		strength: 10,
		health:   100,
		mana:     50,
		level:    1,
	}
}

func (u *Unit) Damage() int {
	return (u.intel + u.agility + u.strength) + (u.level * 2)
}

func (u *Unit) Attack(target *Unit) {
	damage := u.Damage()
	fmt.Printf("%s атакует %s и наносит %d единиц урона.\n", u.name, target.name, damage)
	target.health -= damage
	fmt.Printf("%s теперь имеет %d здоровья.\n", target.name, target.health)
}

func main() {
	warrior := NewUnit()
	warrior.name = "Воин"
	warrior.intel = 5
	warrior.agility = 15
	warrior.strength = 30

	mage := NewUnit()
	mage.name = "Маг"
	mage.intel = 35
	mage.agility = 10
	mage.strength = 5

	warrior.Attack(mage)
	mage.Attack(warrior)
}
