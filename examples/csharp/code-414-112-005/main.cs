// using гарантирует вызов Dispose даже при исключении
public async Task<IEnumerable<User>> GetUsersAsync()
{
    await using var connection = new SqlConnection(_connectionString);
    await connection.OpenAsync();
    
    await using var command = new SqlCommand("SELECT * FROM Users", connection);
    command.CommandTimeout = 30;
    
    await using var reader = await command.ExecuteReaderAsync();
    var users = new List<User>();
    while (await reader.ReadAsync())
    {
        users.Add(MapUser(reader));
    }
    return users;
}
