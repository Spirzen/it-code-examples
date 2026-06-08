// Пример работы с состоянием объектов
using (var context = new AppDbContext())
{
    // Загрузка объекта
    var order = context.Orders.Find(123);
    
    // Проверка состояния
    if (context.Entry(order).State == EntityState.Modified)
    {
        // Объект уже отслеживается как измененный
        Console.WriteLine("Объект изменен");
    }
    
    // Явное изменение статуса
    context.Entry(order).State = EntityState.Deleted;
    
    // Сохранение изменений
    context.SaveChanges();
}
