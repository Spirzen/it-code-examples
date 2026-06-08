Imports System
Imports System.IO

Module Program
    Sub Main()
        Console.OutputEncoding = Text.Encoding.UTF8
        Console.Write("Имя: ")
        Dim userName = Console.ReadLine()

        Console.Write("Возраст: ")
        Dim rawAge = Console.ReadLine()
        Dim age As Integer

        If Integer.TryParse(rawAge, age) Then
            If age >= 18 Then
                Console.WriteLine($"Здравствуйте, {userName}. Доступ разрешён.")
            Else
                Console.WriteLine($"Здравствуйте, {userName}. Доступ ограничен по возрасту.")
            End If
        Else
            Console.WriteLine("Возраст должен быть числом.")
        End If

        Dim logPath = Path.Combine(AppContext.BaseDirectory, "run.log")
        File.AppendAllText(logPath, $"{Date.Now}: запуск приложения{Environment.NewLine}")
        Console.WriteLine("Готово. Нажмите Enter.")
        Console.ReadLine()
    End Sub
End Module
