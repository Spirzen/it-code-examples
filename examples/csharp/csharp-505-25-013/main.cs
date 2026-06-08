public class Animal
{
    protected string Name;

    protected Animal(string name)
    {
        Name = name;
    }

    protected virtual void MakeSound()
    {
        Console.WriteLine("Звук...");
    }
}

public class Dog : Animal
{
    public Dog(string name) : base(name) { }

    protected override void MakeSound()
    {
        Console.WriteLine($"{Name} лает!");
    }
}
