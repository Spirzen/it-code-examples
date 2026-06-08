public class Person
{
    // Автосвойство (поле создаётся автоматически)
    public string Name { get; set; }
    
    // Только для чтения (можно задать в конструкторе, потом нет)
    public int Id { get; }
    
    // Вычисляемое свойство
    public string Greeting => $"Привет, {Name}!";
    
    // Полный синтаксис с полем
    private int _age;
    public int Age 
    { 
        get => _age;
        set 
        {
            if (value < 0) throw new ArgumentException();
            _age = value;
        }
    }
    
    // Инициализаторы свойств
    public List<string> Tags { get; set; } = new List<string>();
}
