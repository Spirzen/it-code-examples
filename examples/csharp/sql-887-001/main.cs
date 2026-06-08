using Microsoft.Data.Sqlite;

var cs = new SqliteConnectionStringBuilder
{
    DataSource = "app.db",
    Mode = SqliteOpenMode.ReadWriteCreate
}.ToString();

using var conn = new SqliteConnection(cs);
conn.Open();

using (var cmd = conn.CreateCommand())
{
    cmd.CommandText = """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
    """;
    cmd.ExecuteNonQuery();
}

using (var tx = conn.BeginTransaction())
{
    var insert = conn.CreateCommand();
    insert.Transaction = tx;
    insert.CommandText = "INSERT INTO users(name) VALUES ($name)";
    insert.Parameters.AddWithValue("$name", "Anna");
    insert.ExecuteNonQuery();
    tx.Commit();
}

var select = conn.CreateCommand();
select.CommandText = "SELECT id, name FROM users";
using var reader = select.ExecuteReader();
while (reader.Read())
{
    Console.WriteLine($"{reader["id"]}: {reader["name"]}");
}
