using System;

class Calculator
{
    static void Main()
    {
        Console.Write("Введите первое число: ");
        if (!double.TryParse(Console.ReadLine(), out double num1))
        {
            Console.WriteLine("Ошибка: Неверный формат первого числа.");
            return;
        }

        Console.Write("Выберите операцию (+, -, *, /): ");
        string operation = Console.ReadLine();

        Console.Write("Введите второе число: ");
        if (!double.TryParse(Console.ReadLine(), out double num2))
        {
            Console.WriteLine("Ошибка: Неверный формат второго числа.");
            return;
        }

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
                if (num2 == 0)
                {
                    Console.WriteLine("Ошибка: Деление на ноль невозможно.");
                    validOperation = false;
                }
                else
                {
                    result = num1 / num2;
                }
                break;
            default:
                Console.WriteLine("Ошибка: Неизвестная операция.");
                validOperation = false;
                break;
        }

        if (validOperation)
        {
            Console.WriteLine($"Результат: {result}");
        }
    }
}
