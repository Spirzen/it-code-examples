using Система;

class SimpleCalculator
{
    static void Main()
    {
        Console.WriteLine("=== Простой калькулятор ===");
        Console.Write("Введите первое число: ");
        double num1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Введите операцию (+, -, *, /): ");
        string operation = Console.ReadLine();

        Console.Write("Введите второе число: ");
        double num2 = Convert.ToDouble(Console.ReadLine());

        double result = 0;
        bool validOperation = true;

        switch (operation)
        {
            case "+":
                result = num1 + num2;
                break;
            case "-":
                result = num1 - num2;
                break;
            case "*":
                result = num1 * num2;
                break;
            case "/":
                if (num2 != 0)
                    result = num1 / num2;
                else
                {
                    Console.WriteLine("Ошибка: деление на ноль.");
                    return;
                }
                break;
            default:
                validOperation = false;
                Console.WriteLine("Неизвестная операция.");
                break;
        }

        if (validOperation)
            Console.WriteLine($"Результат: {num1} {operation} {num2} = {result}");
    }
}
