interface IDrawable
{
    void Draw();
}

class Circle : IDrawable
{
    public void Draw() => Console.WriteLine("Circle");
}

class Square : IDrawable
{
    public void Draw() => Console.WriteLine("Square");
}
