using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class TextSorter
{
    static void Main(string[] args)
    {
        if (args.Length < 2)
        {
            Console.WriteLine("Использование: SortText.exe <input_file> <output_file>");
            return;
        }

        string inputFile = args[0];
        string outputFile = args[1];

        if (!File.Exists(inputFile))
        {
            Console.WriteLine("Ошибка: Входной файл не найден.");
            return;
        }

        // Чтение всех строк из файла
        List<string> lines = File.ReadAllLines(inputFile).ToList();

        // Сортировка строк по алфавиту (независимо от регистра)
        lines.Sort((a, b) => string.Compare(a, b, StringComparison.OrdinalIgnoreCase));

        // Запись отсортированных строк
        File.WriteAllLines(outputFile, lines);

        Console.WriteLine($"Файл '{outputFile}' успешно создан с {lines.Count} строками.");
    }
}
