public static class MathUtils          // static class — нельзя создать экземпляр
{
    public const double PI = 3.14159;  // константа (неявно static)
    
    public static int Square(int x) => x * x;
    
    static MathUtils()                 // статический конструктор (вызывается 1 раз)
    {
        Console.WriteLine("Класс загружен");
    }
}

// Использование (как в Java)
int result = MathUtils.Square(5);
