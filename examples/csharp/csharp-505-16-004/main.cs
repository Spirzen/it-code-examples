using System;
using Serilog;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            // Инициализация логгера
            Log.Logger = new LoggerConfiguration()
                .WriteTo.Console()
                .CreateLogger();

            try
            {
                Log.Information("Запуск приложения");

                var service = new HelloService();
                var message = service.GetMessage();
                Console.WriteLine(message);

                Log.Information("Сообщение выведено: {Message}", message);

                Console.WriteLine("Нажмите любую клавишу для выхода...");
                Console.ReadLine();
            }
            catch (Exception ex)
            {
                Log.Fatal(ex, "Ошибка при выполнении программы");
            }
            finally
            {
                Log.CloseAndFlush(); // Важно!
            }
        }
    }
}
