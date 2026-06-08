public class Person
{
    private string name;

    // Разрешение конфликта имён
    public Person(string name)
    {
        this.name = name; // this.name — поле, name — параметр
    }

    // Вызов другого конструктора
    public Person() : this("Anonymous") { }

    // Передача текущего объекта
    public void PrintInfo()
    {
        Console.WriteLine($"Имя: {this.name}");
    }

    // Возврат самого себя (для цепочки вызовов)
    public Person SetName(string name)
    {
        this.name = name;
        return this;
    }
}
