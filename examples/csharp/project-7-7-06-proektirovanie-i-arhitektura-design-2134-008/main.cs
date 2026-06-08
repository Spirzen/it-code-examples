// Потоковая передача результатов из базы данных
public async IAsyncEnumerable<User> StreamUsersAsync(
    [EnumeratorCancellation] CancellationToken ct)
{
    await using var connection = new SqlConnection(_connectionString);
    await connection.OpenAsync(ct);
    
    await using var command = new SqlCommand(
        "SELECT Id, Name, Email FROM Users ORDER BY Id", 
        connection);
    command.CommandTimeout = 300;
    
    await using var reader = await command.ExecuteReaderAsync(
        CommandBehavior.SequentialAccess, ct);
    
    while (await reader.ReadAsync(ct))
    {
        yield return new User
        {
            Id = reader.GetInt32(0),
            Name = reader.GetString(1),
            Email = reader.GetString(2)
        };
    }
}
