// struct — значимый тип (копируется по значению; локальные переменные часто на стеке, поля класса — в куче вместе с объектом)
public struct Point
{
    public int X { get; set; }
    public int Y { get; set; }
    
    public Point(int x, int y) { X = x; Y = y; }
    
    // record struct (C# 9+) — неизменяемая структура
}

var p1 = new Point(10, 20);
var p2 = p1;        // КОПИЯ значения, а не ссылки
p2.X = 30;          // p1.X остаётся 10
