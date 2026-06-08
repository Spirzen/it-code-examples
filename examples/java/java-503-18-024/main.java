public abstract class Shape {
    public abstract double area();

    public void printArea() {
        System.out.println("Area: " + area());
    }
}

public class Circle extends Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }
}
