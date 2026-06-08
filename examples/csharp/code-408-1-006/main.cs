public class Point {
    public double X { get; }
    public double Y { get; }

    private Point(double x, double y) {
        X = x; Y = y;
    }

    // Фабричный метод
    public static Point CreateOrigin() => new Point(0, 0);
    public static Point FromPolar(double radius, double angle) => 
        new Point(radius * Math.Cos(angle), radius * Math.Sin(angle));
}
