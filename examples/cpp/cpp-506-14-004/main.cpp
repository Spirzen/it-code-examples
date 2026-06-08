class MathUtils {
public:
    // const-метод — не меняет состояние объекта
    int getValue() const { 
        // level++;  // Ошибка! const-метод не может менять поля
        return level;
    }
    
    // Не const-метод — может менять
    void setValue(int val) { 
        level = val; 
    }
    
private:
    int level;
};

// const-параметры и const-переменные
void process(const Warrior& w) {   // const& — не копируем, не меняем
    // w.attack();  // Можно, если attack() — const-метод
    // w.setLevel(5); // Ошибка! const объект
}
