class Rectangle {
private:
    double width, height;

public:
    Rectangle(double w, double h) : width(w), height(h) {}

    double area() const {
        return width * height;
    }

    void scale(double factor) {
        width *= factor;
        height *= factor;
    }
};
