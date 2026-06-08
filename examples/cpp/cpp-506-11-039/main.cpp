#include <iostream>
#include <string>

struct Person {
    std::string name;
    int age;
};

int main() {
    Person p;
    p.name = "Анна";
    p.age = 30;

    std::cout << p.name << ", " << p.age << " лет" << std::endl;

    return 0;
}
