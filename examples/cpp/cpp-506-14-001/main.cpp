#include <string>
#include <iostream>

class Warrior {
private:
    std::string name;
    int level;
    static int count;                    // статическое поле (общее для всех)
    
public:
    // Конструктор с инициализацией (список инициализации — ВАЖНО!)
    Warrior(const std::string& name, int level = 1) 
        : name(name), level(level) {     // ← список инициализации
        count++;
    }
    
    // Виртуальный деструктор (ОБЯЗАТЕЛЬНО для полиморфизма!)
    virtual ~Warrior() {                 // virtual — для корректного удаления
        count--;
    }
    
    // Геттеры (константные методы — не меняют объект)
    std::string getName() const { return name; }
    int getLevel() const { return level; }
    
    // Статический метод
    static int getCount() { return count; }
    
    // Виртуальный метод (для переопределения)
    virtual void attack() const {
        std::cout << name << " атакует! (ур. " << level << ")" << std::endl;
    }
    
    // Чисто виртуальный метод (как abstract в Java)
    virtual void specialAbility() const = 0;  // = 0 → абстрактный метод
};

// Инициализация статического поля (ОБЯЗАТЕЛЬНО вне класса!)
int Warrior::count = 0;

// Warrior абстрактен (есть pure virtual specialAbility) — напрямую
// Warrior w("Имя", 1);  // ошибка компиляции; нужен производный класс, например Knight
