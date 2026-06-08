template<typename Derived>
class Comparable {
public:
    bool operator!=(const Derived& other) const {
        return !static_cast<const Derived*>(this)->operator==(other);
    }
};

class Point : public Comparable<Point> {
    int x, y;
public:
    bool operator==(const Point& p) const {
        return x == p.x && y == p.y;
    }
};
