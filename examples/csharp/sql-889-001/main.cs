using MySqlConnector;

var cs = "Server=localhost;Port=3306;User ID=app_user;Password=secret;Database=app_db;";
await using var conn = new MySqlConnection(cs);
await conn.OpenAsync();

await using (var cmd = new MySqlCommand("""
    CREATE TABLE IF NOT EXISTS users(
      id BIGINT PRIMARY KEY AUTO_INCREMENT,
      name VARCHAR(255) NOT NULL
    ) ENGINE=InnoDB
""", conn))
{
    await cmd.ExecuteNonQueryAsync();
}

await using (var ins = new MySqlCommand("INSERT INTO users(name) VALUES (@name)", conn))
{
    ins.Parameters.AddWithValue("@name", "Anna");
    await ins.ExecuteNonQueryAsync();
}

await using (var sel = new MySqlCommand("SELECT id, name FROM users", conn))
await using (var reader = await sel.ExecuteReaderAsync())
{
    while (await reader.ReadAsync())
        Console.WriteLine($"{reader.GetInt64(0)} {reader.GetString(1)}");
}
