#include <iostream>
#include <string>

class Animal {
public:
    std::string name;

    explicit Animal(const std::string& name) : name(name) {}

    void eat() const {
        std::cout << name << " ест" << std::endl;
    }
};

class Cat : public Animal {
public:
    explicit Cat(const std::string& name) : Animal(name) {}

    void speak() const {
        std::cout << "Мяу!" << std::endl;
    }
};

class Dog : public Animal {
public:
    explicit Dog(const std::string& name) : Animal(name) {}

    void speak() const {
        std::cout << "Гав!" << std::endl;
    }
};

int main() {
    Cat cat("Мурка");
    Dog dog("Шарик");
    cat.eat();
    cat.speak();
    dog.eat();
    dog.speak();
    return 0;
}
