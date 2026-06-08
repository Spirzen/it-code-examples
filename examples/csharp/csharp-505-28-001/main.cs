class User
{
    public int Id { get; set; }
    public string Name { get; set; }
}

// Создаём коллекцию пользователей
var users = new List<User>
{
    new User { Id = 1, Name = "Alice" },
    new User { Id = 2, Name = "Bob" },
    new User { Id = 3, Name = "Charlie" }
};

// Обрабатываем всех пользователей
foreach (var user in users)
{
    Console.WriteLine($"Hello, {user.Name}!");
}
