public class Animal
{
    public Animal(string name)
    {
        Name = name;
    }
}

public class Dog : Animal
{
    public Dog(string name) : base(name) // вызов конструктора Animal
    {
        // дополнительная инициализация
    }
}
