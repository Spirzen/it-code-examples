using var context = new AppDbContext();

// Создание базы и таблиц (если не существует)
context.Database.EnsureCreated();

// Добавление пользователя
var user = new User
{
    Name = "Боб",
    Email = "bob@example.com",
    Age = 34
};
context.Users.Add(user);
context.SaveChanges();

// Чтение всех пользователей
var allUsers = context.Users.ToList();
foreach (var u in allUsers)
{
    Console.WriteLine($"ID: {u.Id}, Имя: {u.Name}, Email: {u.Email}, Возраст: {u.Age}");
}
