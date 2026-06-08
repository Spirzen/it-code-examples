using System;

public class Unit
{
    public string Name = "Имя";
    public int Intel = 10;
    public int Agility = 10;
    public int Strength = 10;
    public int Health = 100;
    public int Mana = 50;
    public int Level = 1;

    public int Damage
    {
        get { return (Intel + Agility + Strength) + (Level * 2); }
    }

    public void Attack(Unit target)
    {
        Console.WriteLine($"{Name} атакует {target.Name} и наносит {Damage} единиц урона.");
        target.Health -= Damage;
        Console.WriteLine($"{target.Name} теперь имеет {target.Health} здоровья.");
    }

    public static void Main(string[] args)
    {
        Unit warrior = new Unit();
        warrior.Name = "Воин";
        warrior.Intel = 5;
        warrior.Agility = 15;
        warrior.Strength = 30;

        Unit mage = new Unit();
        mage.Name = "Маг";
        mage.Intel = 35;
        mage.Agility = 10;
        mage.Strength = 5;

        warrior.Attack(mage);
        mage.Attack(warrior);
    }
}
