public class Warrior
{
    // Поля (обычно private)
    private string _name;
    private static int _count = 0;
    public int Strength { get; set; } = 10;
    public int Agility { get; set; } = 10;
    
    // Автосвойство (компилятор сам создаст поле)
    public int Level { get; set; } = 1;
    
    // Свойство с логикой
    public string Name 
    { 
        get => _name;
        set 
        {
            if (string.IsNullOrEmpty(value))
                throw new ArgumentException("Имя не может быть пустым");
            _name = value;
        }
    }
    
    // Вычисляемое свойство (только get)
    public int Damage => (Strength + Agility) + Level * 2;
    
    // Статическое свойство
    public static int Count => _count;
    
    // Конструктор
    public Warrior(string name, int level = 1)  // опциональный параметр
    {
        Name = name;
        Level = level;
        _count++;
    }
    
    // Переопределение ToString()
    public override string ToString() => $"Воин: {Name} (ур. {Level})";
}

// Использование
var warrior = new Warrior("Артур", 5);
warrior.Level = 10;
Console.WriteLine(warrior.Damage);
