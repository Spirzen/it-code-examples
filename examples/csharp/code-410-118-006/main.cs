// Пример использования пользовательской транзакции
using (var context = new AppDbContext())
using (var transaction = context.Database.BeginTransaction())
{
    try
    {
        // Операция 1
        var user = new User { Name = "Новый пользователь" };
        context.Users.Add(user);
        
        // Операция 2
        var order = new Order { UserId = user.Id, TotalAmount = 100 };
        context.Orders.Add(order);
        
        // Операция 3
        await context.SaveChangesAsync();
        
        // Фиксация транзакции
        transaction.Commit();
    }
    catch (Exception)
    {
        // Откат транзакции при ошибке
        transaction.Rollback();
        throw;
    }
}
