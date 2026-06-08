using Microsoft.Data.Sqlite;
using BooksAdo.Models;

const string cs = "Data Source=books_ado.db";

await using (var conn = new SqliteConnection(cs))
{
    await conn.OpenAsync();

    var create = """
        CREATE TABLE IF NOT EXISTS Books (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Year INTEGER NOT NULL
        );
        """;
    await using (var cmd = new SqliteCommand(create, conn))
        await cmd.ExecuteNonQueryAsync();

    const string insert = "INSERT INTO Books (Title, Year) VALUES (@title, @year);";
    await using var insertCmd = new SqliteCommand(insert, conn);
    insertCmd.Parameters.AddWithValue("@title", "Clean Code");
    insertCmd.Parameters.AddWithValue("@year", 2008);
    await insertCmd.ExecuteNonQueryAsync();
}
