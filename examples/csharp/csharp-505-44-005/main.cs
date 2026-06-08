public class User
{
    public int Id { get; set; } // Первичный ключ
    public string Name { get; set; }
    public int Age { get; set; }
}

public class Order
{
    public int Id { get; set; }
    public string ProductName { get; set; }
    public int UserId { get; set; } // Внешний ключ
    public User User { get; set; } // Навигационное свойство
}
