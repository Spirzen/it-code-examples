using System.Diagnostics;

// Создание снимка памяти
var snapshot1 = Process.GetCurrentProcess().WorkingSet64;

// Выполнение кода
ProcessData();

// Второй снимок
var snapshot2 = Process.GetCurrentProcess().WorkingSet64;

Console.WriteLine($"Использовано памяти: {(snapshot2 - snapshot1) / 1024 / 1024} МБ");
