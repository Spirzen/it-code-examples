await using var conn = new NpgsqlConnection(connectionString);
await conn.OpenAsync();

await using var tx = await conn.BeginTransactionAsync();

await using (var cmd = new NpgsqlCommand(
    "INSERT INTO teams (id, name, lead_id) VALUES (1, 'Backend', 42)", conn, tx))
{
    await cmd.ExecuteNonQueryAsync();
}

await using (var cmd = new NpgsqlCommand(
    "INSERT INTO employees (id, name, team_id) VALUES (42, 'Иван', 1)", conn, tx))
{
    await cmd.ExecuteNonQueryAsync();
}

await tx.CommitAsync();
