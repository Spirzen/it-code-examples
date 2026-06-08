// Контракт "умения лечить" — только heal(), без второго attack()
class Healable {
public:
    virtual void heal() const = 0;
    virtual ~Healable() = default;
};

// Knight уже наследует Warrior и реализует attack() const
class Paladin : public Knight, public Healable {
public:
    Paladin(const std::string& name, const std::string& horse, int level = 1)
        : Knight(name, horse, level) {}

    void attack() const override {
        std::cout << getName() << " атакует священным мечом!\n";
    }

    void heal() const override {
        std::cout << getName() << " использует исцеление!\n";
    }

    void specialAbility() const override {
        std::cout << "Светлая защита!\n";
    }
};
