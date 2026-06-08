public class Unit {
    String name = "Имя";
    int intel = 10;
    int agility = 10;
    int strength = 10;
    int health = 100;
    int mana = 50;
    int level = 1;

    public int getDamage() {
        return (intel + agility + strength) + (level * 2);
    }

    public void attack(Unit target) {
        System.out.println(name + " атакует " + target.name + " и наносит " + getDamage() + " единиц урона.");
        target.health -= getDamage();
        System.out.println(target.name + " теперь имеет " + target.health + " здоровья.");
    }

    public static void main(String[] args) {
        Unit warrior = new Unit();
        warrior.name = "Воин";
        warrior.intel = 5;
        warrior.agility = 15;
        warrior.strength = 30;

        Unit mage = new Unit();
        mage.name = "Маг";
        mage.intel = 35;
        mage.agility = 10;
        mage.strength = 5;

        warrior.attack(mage);
        mage.attack(warrior);
    }
}
