class Smartphone
{
    private readonly string model;
    private int battery;

    public Smartphone(string model)
    {
        this.model = model;
        battery = 20;
    }

    public void Call()
    {
        battery = Math.Max(0, battery - 5);
        Console.WriteLine($"Звонок с {model}... Заряд: {battery}%");
    }

    public void Charge()
    {
        battery = Math.Min(100, battery + 30);
        Console.WriteLine($"Зарядка {model}... Заряд: {battery}%");
    }

    public void ShowStatus()
    {
        Console.WriteLine($"Смартфон {model}: заряд {battery}%");
    }
}

class Program
{
    static void Main()
    {
        var phone = new Smartphone("Pixel");
        phone.ShowStatus();
        phone.Call();
        phone.Charge();
        phone.ShowStatus();
    }
}
