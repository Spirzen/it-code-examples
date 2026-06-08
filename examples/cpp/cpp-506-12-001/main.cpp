class Vector2D {
    double x_, y_;
public:
    Vector2D(double x, double y) : x_(x), y_(y) {}

    // Перегрузка + как функция-член
    Vector2D operator+(const Vector2D& other) const {
        return Vector2D(x_ + other.x_, y_ + other.y_);
    }
};

// Или как свободная функция:
Vector2D operator+(const Vector2D& a, const Vector2D& b) {
    return Vector2D(a.x() + b.x(), a.y() + b.y());
}
