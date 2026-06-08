using Система;

public class Calculator
{
    public double Add(double a, double b) => a + b;
    public double Subtract(double a, double b) => a - b;
    public double Multiply(double a, double b) => a * b;
    public double Divide(double a, double b)
    {
        if (b == 0) throw new DivideByZeroException("Деление на ноль невозможно.");
        return a / b;
    }

    public double? Calculate(double a, string operation, double b)
    {
        return operation switch
        {
            "+" => Add(a, b),
            "-" => Subtract(a, b),
            "*" => Multiply(a, b),
            "/" => Divide(a, b),
            _ => null
        };
    }
}

class Program
{
    static void Main()
    {
        var calc = new Calculator();
        Console.WriteLine("=== ООП-калькулятор ===");

        while (true)
        {
            try
            {
                Console.Write("Число 1 (или 'q' для выхода): ");
                string s1 = Console.ReadLine();
                if (s1 == "q") break;

                double x = double.Parse(s1);
                Console.Write("Операция (+, -, *, /): ");
                string op = Console.ReadLine();
                Console.Write("Число 2: ");
                double y = double.Parse(Console.ReadLine());

                double? res = calc.Calculate(x, op, y);
                if (res.HasValue)
                    Console.WriteLine($"= {res.Value}");
                else
                    Console.WriteLine("Неизвестная операция.");
            }
            catch (DivideByZeroException ex)
            {
                Console.WriteLine($"Ошибка: {ex.Message}");
            }
            catch (FormatException)
            {
                Console.WriteLine("Ошибка: введите корректное число.");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Неожиданная ошибка: {ex.Message}");
            }

            Console.WriteLine();
        }
    }
}
