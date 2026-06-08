string day = "понедельник";

switch (day)
{
    case "понедельник":
        Console.WriteLine("Начало недели");
        break;
    case "пятница":
        Console.WriteLine("Почти выходные");
        break;
    case "суббота":
    case "воскресенье":
        Console.WriteLine("Выходные!");
        break;
    default:
        Console.WriteLine("Обычный день");
        break;
}
