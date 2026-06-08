class Vector2 {
public:
    int x, y;
    
    Vector2(int x, int y) : x(x), y(y) {}
    
    // Перегрузка оператора +
    Vector2 operator+(const Vector2& other) const {
        return Vector2(x + other.x, y + other.y);
    }
    
    // Перегрузка оператора ==
    bool operator==(const Vector2& other) const {
        return x == other.x && y == other.y;
    }
    
    // Перегрузка оператора [] (как в массиве)
    int operator[](int index) const {
        return index == 0 ? x : y;
    }
};

// Использование
Vector2 v1(1, 2), v2(3, 4);
Vector2 v3 = v1 + v2;   // (4, 6)
if (v1 == v2) { /* ... */ }
