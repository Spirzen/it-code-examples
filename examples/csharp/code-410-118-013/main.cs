// Пример безопасной работы с ORM
public async Task CreateUserAsync(string username, string password)
{
    // Хеширование пароля перед сохранением
    var hashedPassword = PasswordHasher.Hash(password);
    
    var user = new User 
    { 
        Username = username, 
        PasswordHash = hashedPassword 
    };
    
    // Проверка прав доступа
    if (!await CurrentUserService.HasPermissionAsync(Permission.CreateUser))
    {
        throw new UnauthorizedAccessException("Нет прав на создание пользователя");
    }
    
    // Добавление пользователя
    _context.Users.Add(user);
    await _context.SaveChangesAsync();
}

// Пример предотвращения SQL-инъекций
public async Task SearchUsersAsync(string searchTerm)
{
    // Безопасный запрос с параметрами
    var users = await _context.Users
        .Where(u => u.Username.Contains(searchTerm))
        .ToListAsync();
        
    // Небезопасный подход (избегать!)
    // var users = await _context.Users
    //     .FromSqlRaw($"SELECT * FROM Users WHERE Username LIKE '%{searchTerm}%'")
    //     .ToListAsync();
}
