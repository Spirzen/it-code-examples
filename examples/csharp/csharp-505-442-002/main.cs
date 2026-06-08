await using var conn = new SqliteConnection(cs);
await conn.OpenAsync();

await using var cmd = new SqliteCommand(
    "SELECT Id, Title, Year FROM Books WHERE Year >= @y ORDER BY Title;",
    conn);
cmd.Parameters.AddWithValue("@y", 2000);

await using var reader = await cmd.ExecuteReaderAsync();
while (await reader.ReadAsync())
{
    var id = reader.GetInt32(0);
    var title = reader.GetString(1);
    var year = reader.GetInt32(2);
    Console.WriteLine($"{id}: {title} ({year})");
}
