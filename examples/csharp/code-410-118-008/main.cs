// Пример обработки исключений ORM
try
{
    using (var context = new AppDbContext())
    {
        var user = new User { Name = "Иван", Email = "ivan@example.com" };
        context.Users.Add(user);
        await context.SaveChangesAsync();
    }
}
catch (DbUpdateConcurrencyException ex)
{
    // Обработка конфликта версий
    Console.WriteLine($"Конфликт версий: {ex.Message}");
}
catch (DbUpdateException ex)
{
    // Обработка ошибок сохранения
    Console.WriteLine($"Ошибка сохранения: {ex.InnerException?.Message}");
}
catch (SqlException ex)
{
    // Обработка ошибок SQL
    Console.WriteLine($"Ошибка SQL: {ex.Number} - {ex.Message}");
}
catch (TimeoutException ex)
{
    // Обработка таймаутов
    Console.WriteLine($"Таймаут: {ex.Message}");
}
