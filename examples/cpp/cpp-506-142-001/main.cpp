#include <typeinfo>
#include <iostream>

class Base {
public:
    virtual ~Base() = default;
};

class Derived : public Base {};

void print_type(const Base& obj) {
    const std::type_info& ti = typeid(obj);
    std::cout << ti.name() << '\n';
}

int main() {
    Derived d;
    print_type(d);
    std::cout << (typeid(d) == typeid(Derived)) << '\n';
}
