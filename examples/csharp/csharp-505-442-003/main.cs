await using var conn = new SqliteConnection(cs);
await conn.OpenAsync();
await using var tx = await conn.BeginTransactionAsync();

try
{
    await conn.ExecuteAsync(
        "INSERT INTO Books (Title, Year) VALUES (@Title, @Year);",
        new { Title = "Book A", Year = 2020 },
        transaction: tx);
    await conn.ExecuteAsync(
        "INSERT INTO Books (Title, Year) VALUES (@Title, @Year);",
        new { Title = "Book B", Year = 2021 },
        transaction: tx);
    await tx.CommitAsync();
}
catch
{
    await tx.RollbackAsync();
    throw;
}
