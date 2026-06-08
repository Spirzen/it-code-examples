#include <iostream>
#include <string>

class Unit {
    std::string name_;
    int intel_;
    int agility_;
    int strength_;
    int health_;
    int mana_;
    int level_;

public:
    Unit()
        : name_("Имя"), intel_(10), agility_(10), strength_(10),
          health_(100), mana_(50), level_(1) {}

    void setName(const std::string& name) { name_ = name; }
    void setStats(int intel, int agility, int strength) {
        intel_ = intel;
        agility_ = agility;
        strength_ = strength;
    }

    const std::string& name() const { return name_; }
    int health() const { return health_; }

    int getDamage() const {
        return (intel_ + agility_ + strength_) + (level_ * 2);
    }

    void takeDamage(int amount) {
        health_ -= amount;
    }

    void attack(Unit& target) {
        const int dmg = getDamage();
        std::cout << name_ << " атакует " << target.name_
                  << " и наносит " << dmg << " единиц урона.\n";
        target.takeDamage(dmg);
        std::cout << target.name_ << " теперь имеет "
                  << target.health_ << " здоровья.\n";
    }
};

int main() {
    Unit warrior;
    warrior.setName("Воин");
    warrior.setStats(5, 15, 30);

    Unit mage;
    mage.setName("Маг");
    mage.setStats(35, 10, 5);

    warrior.attack(mage);
    mage.attack(warrior);

    return 0;
}
