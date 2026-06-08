using Система;
using Система.data.SQLite;

class AdoNetExample
{
    private const string ConnectionString = "Data Source=users.db;Version=3;";

    static void Main()
    {
        // Создание таблицы
        CreateUsersTable();

        // Вставка записи
        InsertUser("Алиса", "alice@example.com", 28);

        // Чтение всех записей
        ReadAllUsers();
    }

    static void CreateUsersTable()
    {
        using var connection = new SQLiteConnection(ConnectionString);
        connection.Open();

        string sql = @"
            CREATE TABLE IF NOT EXISTS Users (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Email TEXT NOT NULL UNIQUE,
                Age INTEGER
            );";

        using var command = new SQLiteCommand(sql, connection);
        command.ExecuteNonQuery();
    }

    static void InsertUser(string name, string email, int age)
    {
        using var connection = new SQLiteConnection(ConnectionString);
        connection.Open();

        string sql = "INSERT INTO Users (Name, Email, Age) VALUES (@name, @email, @age);";

        using var command = new SQLiteCommand(sql, connection);
        command.Parameters.AddWithValue("@name", name);
        command.Parameters.AddWithValue("@email", email);
        command.Parameters.AddWithValue("@age", age);

        int rowsAffected = command.ExecuteNonQuery();
        Console.WriteLine($"Добавлено строк: {rowsAffected}");
    }

    static void ReadAllUsers()
    {
        using var connection = new SQLiteConnection(ConnectionString);
        connection.Open();

        string sql = "SELECT Id, Name, Email, Age FROM Users;";
        using var command = new SQLiteCommand(sql, connection);
        using var reader = command.ExecuteReader();

        while (reader.Read())
        {
            int id = reader.GetInt32("Id");
            string name = reader.GetString("Name");
            string email = reader.GetString("Email");
            int age = reader.GetInt32("Age");

            Console.WriteLine($"ID: {id}, Имя: {name}, Email: {email}, Возраст: {age}");
        }
    }
}
