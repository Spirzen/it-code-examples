Option Explicit On
Option Strict On
Option Infer On

Imports System

Module Program
    Sub Main()
        Console.Write("Введите число: ")
        Dim raw = Console.ReadLine()
        Dim number As Integer

        If Integer.TryParse(raw, number) Then
            Console.WriteLine($"Квадрат: {number * number}")
        Else
            Console.WriteLine("Нужно ввести целое число.")
        End If
    End Sub
End Module
