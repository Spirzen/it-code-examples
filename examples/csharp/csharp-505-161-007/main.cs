using System;
using System.IO;

class DirectoryScanner
{
    static void Main(string[] args)
    {
        if (args.Length < 1)
        {
            Console.WriteLine("Укажите путь к директории.");
            return;
        }

        string rootPath = args[0];
        
        if (!Directory.Exists(rootPath))
        {
            Console.WriteLine("Директория не найдена.");
            return;
        }

        string[] files = Directory.GetFiles(rootPath, "*", SearchOption.AllDirectories);

        Console.WriteLine($"Найдено файлов: {files.Length}");
        long totalSize = 0;

        foreach (string file in files)
        {
            FileInfo info = new FileInfo(file);
            totalSize += info.Length;
            
            // Ограничим вывод первых 10 файлов для краткости
            if (Array.IndexOf(files, file) < 10)
            {
                Console.WriteLine($"{info.Name} ({info.Length} байт)");
            }
        }

        Console.WriteLine($"Общий размер: {totalSize / 1024.0:F2} КБ");
    }
}
