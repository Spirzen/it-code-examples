// Правильно
public IReadOnlyList<User> GetActiveUsers()
{
    return _users
        .Where(u => u.IsActive)
        .ToList()
        .AsReadOnly();
}

// Допустимо при использовании yield return
public IEnumerable<User> EnumerateActiveUsers()
{
    foreach (var user in _users)
    {
        if (user.IsActive)
        {
            yield return user;
        }
    }
}
