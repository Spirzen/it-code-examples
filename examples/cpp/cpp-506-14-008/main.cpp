#include <iostream>
#include <memory>

class Animal {
public:
    virtual void sound() {           // virtual — для переопределения
        std::cout << "???" << std::endl;
    }
    virtual ~Animal() = default;     // виртуальный деструктор!
};

class Dog : public Animal {
public:
    void sound() override {          // override — C++11, явно указываем
        std::cout << "Гав!" << std::endl;
    }
};

std::unique_ptr<Animal> a = std::make_unique<Dog>();
a->sound();      // "Гав!" — полиморфизм через vtable
