using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            var service = new HelloService();
            Console.WriteLine(service.GetMessage());

            Console.WriteLine("Нажмите любую клавишу для выхода...");
            Console.ReadLine();
        }
    }
}
