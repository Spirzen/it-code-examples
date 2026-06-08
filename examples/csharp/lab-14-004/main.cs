using Система;
using Система.data.SQLite;
using Dapper;

class DapperExample
{
    private const string ConnectionString = "Data Source=users_dapper.db;Version=3;";

    static void Main()
    {
        using var connection = new SQLiteConnection(ConnectionString);
        connection.Open();

        // Создание таблицы
        connection.Execute(@"
            CREATE TABLE IF NOT EXISTS Users (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Email TEXT NOT NULL UNIQUE,
                Age INTEGER
            );");

        // Вставка
        var userId = connection.Execute(
            "INSERT INTO Users (Name, Email, Age) VALUES (@Name, @Email, @Age);",
            new { Name = "Карина", Email = "karina@example.com", Age = 25 });

        // Чтение
        var users = connection.Query<User>("SELECT * FROM Users;");
        foreach (var u in users)
        {
            Console.WriteLine($"ID: {u.Id}, Имя: {u.Name}, Email: {u.Email}, Возраст: {u.Age}");
        }
    }
}

public class User
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public string Email { get; set; } = string.Empty;
    public int Age { get; set; }
}
