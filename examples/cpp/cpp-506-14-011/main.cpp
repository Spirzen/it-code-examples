class Flyable {
public:
    virtual void fly() const = 0;
};

class Swimmable {
public:
    virtual void swim() const = 0;
};

class Duck : public Animal, public Flyable, public Swimmable {
public:
    void speak() const override { std::cout << "Quack!\n"; }
    void fly() const override { std::cout << "Duck is flying\n"; }
    void swim() const override { std::cout << "Duck is swimming\n"; }
};
