// Пример модели данных в C# с использованием Entity Framework
public class User
{
    public int Id { get; set; }
    public string Name { get; set; }
    public DateTime CreatedAt { get; set; }
    
    // Связь один-ко-многим
    public virtual ICollection<Order> Orders { get; set; }
}

public class Order
{
    public int Id { get; set; }
    public int UserId { get; set; }
    public decimal TotalAmount { get; set; }
    
    // Обратная связь
    public virtual User User { get; set; }
}
