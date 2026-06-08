public class Animal
{
    public virtual void MakeSound()
    {
        Console.WriteLine("Звук...");
    }
}

public class Dog : Animal
{
    public override void MakeSound()
    {
        base.MakeSound(); // сначала базовая логика
        Console.WriteLine("Гав!"); // потом своя
    }
}
