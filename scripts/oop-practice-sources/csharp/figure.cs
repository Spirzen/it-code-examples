class Figure
{
    public string Name { get; }
    public string Color { get; }

    public Figure(string name, string color)
    {
        Name = name;
        Color = color;
    }

    public void Describe()
    {
        Console.WriteLine($"Фигура «{Name}», цвет: {Color}");
    }
}

class Circle : Figure
{
    public Circle(string color) : base("Круг", color) { }
}

class Square : Figure
{
    public Square(string color) : base("Квадрат", color) { }
}

class Program
{
    static void Main()
    {
        var circle = new Circle("красный");
        var square = new Square("синий");
        circle.Describe();
        square.Describe();
    }
}
