class Shape {
    public double getArea() {
        return 0.0;
    }
}

class Circle extends Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double getArea() { // тот же тип double
        return Math.PI * radius * radius;
    }
}
