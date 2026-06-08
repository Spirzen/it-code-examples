// Обычное наследование (один родитель)
class Knight : public Warrior {          // public — тип наследования
private:
    std::string horseName;
    
public:
    Knight(const std::string& name, const std::string& horse, int level = 1)
        : Warrior(name, level), horseName(horse) {}
    
    // override — ключевое слово (C++11, для читаемости)
    void attack() const override {
        std::cout << getName() << " на коне " << horseName << " атакует!" << std::endl;
    }
    
    void specialAbility() const override {
        std::cout << "Рыцарский удар!" << std::endl;
    }
};

// МНОЖЕСТВЕННОЕ наследование (того нет в Java/C#)
class Flying { 
public:
    virtual void fly() { std::cout << "Летит" << std::endl; }
};

class Swimming {
public:
    virtual void swim() { std::cout << "Плывёт" << std::endl; }
};

class Duck : public Flying, public Swimming {  // два родителя!
    // Алмазная проблема — если Flying и Swimming наследуют общий класс
};
