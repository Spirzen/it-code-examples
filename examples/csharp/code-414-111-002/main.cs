using System;
using System.Threading;

class Program
{
	static void Main()
	{
		Console.WriteLine("Приложение запущено. Ожидание 30 секунд перед стартом...");
		Thread.Sleep(30_000);

		var name = "Тимур";
		var result = ProcessName(name);
		Console.WriteLine($"Результат: {result}");
		Console.WriteLine("Готово. Нажмите Enter для выхода.");
		Console.ReadLine();
	}

	static string ProcessName(string input)
	{
		// Точка для отладки
		var clean = input?.Trim();
		var upper = clean?.ToUpperInvariant();
		return $"[ОБРАБОТАНО] {upper}";
	}
}
