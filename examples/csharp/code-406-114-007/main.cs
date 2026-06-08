// Плохо: множество мелких запросов
public async Task<List<User>> GetUsersBad(List<int> userIds)
{
    var users = new List<User>();
    foreach (var id in userIds)
    {
        var user = await _httpClient.GetAsync($"api/users/{id}");
        users.Add(await user.Content.ReadAsAsync<User>());
    }
    return users;
}

// Хорошо: пакетный запрос
public async Task<List<User>> GetUsersGood(List<int> userIds)
{
    var response = await _httpClient.PostAsJsonAsync(
        "api/users/batch",
        new { userIds }
    );
    return await response.Content.ReadAsAsync<List<User>>();
}
