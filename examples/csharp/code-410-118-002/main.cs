// Пример жизненного цикла объекта
using (var context = new AppDbContext())
{
    // 1. Создание нового объекта
    var user = new User 
    { 
        Name = "Иван Иванов", 
        CreatedAt = DateTime.Now 
    };
    
    // 2. Добавление в контекст (состояние: Новый -> Отслеживаемый)
    context.Users.Add(user);
    
    // 3. Сохранение в базу данных (состояние: Отслеживаемый -> Загруженный)
    context.SaveChanges();
    
    // 4. Изменение свойства
    user.Name = "Иван Петров";
    
    // 5. Применение изменений
    context.SaveChanges();
    
    // 6. Удаление объекта
    context.Users.Remove(user);
    context.SaveChanges();
}
