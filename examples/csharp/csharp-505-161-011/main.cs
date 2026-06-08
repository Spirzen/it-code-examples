using System;

class DateConverter
{
    static void Main()
    {
        string inputDate = "2025-11-01T14:30:00";
        string formatIn = "yyyy-MM-ddTHH:mm:ss";
        string formatOut = "dd.MM.yyyy HH:mm";

        try
        {
            DateTime dt = DateTime.ParseExact(inputDate, formatIn, null);
            string output = dt.ToString(formatOut);

            Console.WriteLine($"Входная строка: {inputDate}");
            Console.WriteLine($"Выходная строка: {output}");
            Console.WriteLine($"Тип даты: {dt.Kind}");
        }
        catch (FormatException)
        {
            Console.WriteLine("Ошибка: Неправильный формат входной строки.");
        }
    }
}
