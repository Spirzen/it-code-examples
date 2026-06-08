class Example {
private:        // только внутри класса (по умолчанию в class)
    int privateField;
    
protected:      // внутри класса + наследники
    int protectedField;
    
public:         // отовсюду
    int publicField;
};

struct Point {  // struct — всё public по умолчанию (обратная совместимость с C)
    int x, y;   // == public:
};
