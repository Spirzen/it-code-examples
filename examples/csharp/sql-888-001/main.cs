using Npgsql;

var cs = "Host=localhost;Port=5432;Username=app_user;Password=secret;Database=app_db";
await using var conn = new NpgsqlConnection(cs);
await conn.OpenAsync();

await using (var cmd = new NpgsqlCommand("""
    CREATE TABLE IF NOT EXISTS users(
      id BIGSERIAL PRIMARY KEY,
      name TEXT NOT NULL
    )
""", conn))
{
    await cmd.ExecuteNonQueryAsync();
}

await using (var ins = new NpgsqlCommand("INSERT INTO users(name) VALUES (@name)", conn))
{
    ins.Parameters.AddWithValue("name", "Anna");
    await ins.ExecuteNonQueryAsync();
}

await using (var sel = new NpgsqlCommand("SELECT id, name FROM users", conn))
await using (var reader = await sel.ExecuteReaderAsync())
{
    while (await reader.ReadAsync())
        Console.WriteLine($"{reader.GetInt64(0)} {reader.GetString(1)}");
}
