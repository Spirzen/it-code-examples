using System;
using System.IO;
using System.Diagnostics;

class BackupUtility
{
    static void Main(string[] args)
    {
        if (args.Length < 2)
        {
            Console.WriteLine("Использование: Backup.exe <source_folder> <destination_folder>");
            return;
        }

        string source = args[0];
        string destination = args[1];
        string timestamp = DateTime.Now.ToString("yyyyMMdd_HHmmss");
        string backupFolder = Path.Combine(destination, $"Backup_{timestamp}");

        if (!Directory.Exists(source))
        {
            Console.WriteLine("Источник не существует.");
            return;
        }

        Directory.CreateDirectory(backupFolder);
        
        int copiedCount = 0;
        string[] files = Directory.GetFiles(source, "*.*", SearchOption.AllDirectories);

        foreach (string file in files)
        {
            string relativePath = file.Substring(source.Length).TrimStart(Path.DirectorySeparatorChar);
            string destFile = Path.Combine(backupFolder, relativePath);
            
            string destDir = Path.GetDirectoryName(destFile);
            Directory.CreateDirectory(destDir);
            
            File.Copy(file, destFile, true); // true означает перезапись существующих файлов
            copiedCount++;
        }

        Console.WriteLine($"Резервная копия создана в: {backupFolder}");
        Console.WriteLine($"Скопировано файлов: {copiedCount}");
    }
}
