using Система;

class AdvancedCalculator
{
    static void Main()
    {
        Console.WriteLine("=== Расширенный калькулятор ===");
        Console.WriteLine("Поддерживаемые операции: +, -, *, /");
        Console.WriteLine("Введите 'exit', чтобы завершить работу.\n");

        while (true)
        {
            Console.Write("Первое число: ");
            string input1 = Console.ReadLine();
            if (input1?.ToLower() == "exit") break;

            if (!double.TryParse(input1, out double num1))
            {
                Console.WriteLine("Некорректное число. Попробуйте снова.\n");
                continue;
            }

            Console.Write("Операция (+, -, *, /): ");
            string op = Console.ReadLine();
            if (op?.ToLower() == "exit") break;

            Console.Write("Второе число: ");
            string input2 = Console.ReadLine();
            if (input2?.ToLower() == "exit") break;

            if (!double.TryParse(input2, out double num2))
            {
                Console.WriteLine("Некорректное число. Попробуйте снова.\n");
                continue;
            }

            double? result = PerformCalculation(num1, op, num2);
            if (result.HasValue)
            {
                Console.WriteLine($"Результат: {num1} {op} {num2} = {result.Value}\n");
            }
            else
            {
                Console.WriteLine("Ошибка: неверная операция или деление на ноль.\n");
            }
        }

        Console.WriteLine("Работа калькулятора завершена.");
    }

    static double? PerformCalculation(double a, string operation, double b)
    {
        return operation switch
        {
            "+" => a + b,
            "-" => a - b,
            "*" => a * b,
            "/" when b != 0 => a / b,
            _ => null
        };
    }
}
