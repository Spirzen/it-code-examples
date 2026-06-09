class Animal
{
    public string Name { get; }

    public Animal(string name)
    {
        Name = name;
    }

    public void Eat()
    {
        Console.WriteLine($"{Name} ест");
    }
}

class Cat : Animal
{
    public Cat(string name) : base(name) { }

    public void Speak()
    {
        Console.WriteLine("Мяу!");
    }
}

class Dog : Animal
{
    public Dog(string name) : base(name) { }

    public void Speak()
    {
        Console.WriteLine("Гав!");
    }
}

class Program
{
    static void Main()
    {
        var cat = new Cat("Мурка");
        var dog = new Dog("Шарик");
        cat.Eat();
        cat.Speak();
        dog.Eat();
        dog.Speak();
    }
}
