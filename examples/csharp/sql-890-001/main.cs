using Microsoft.Data.SqlClient;

var cs = "Server=localhost,1433;Database=app_db;User Id=app_user;Password=secret;Encrypt=True;TrustServerCertificate=True;";
await using var conn = new SqlConnection(cs);
await conn.OpenAsync();

await using (var cmd = new SqlCommand("""
    IF OBJECT_ID('dbo.Users', 'U') IS NULL
    CREATE TABLE dbo.Users(
      Id BIGINT IDENTITY(1,1) PRIMARY KEY,
      Name NVARCHAR(255) NOT NULL
    );
""", conn))
{
    await cmd.ExecuteNonQueryAsync();
}

await using (var ins = new SqlCommand("INSERT INTO dbo.Users(Name) VALUES (@name)", conn))
{
    ins.Parameters.AddWithValue("@name", "Anna");
    await ins.ExecuteNonQueryAsync();
}

await using (var sel = new SqlCommand("SELECT Id, Name FROM dbo.Users", conn))
await using (var reader = await sel.ExecuteReaderAsync())
{
    while (await reader.ReadAsync())
        Console.WriteLine($"{reader.GetInt64(0)} {reader.GetString(1)}");
}
