using (var db = new MyDb()) {
    // Добавление
    db.Users.Insert(() => new User { Name = "Bob" });

    // Запрос
    var users = db.Users.Where(u => u.Name.StartsWith("B")).ToList();

    // Обновление
    db.Users.Where(u => u.Id == 1)
            .Set(u => u.Name, "Alice")
            .Update();

    // Удаление
    db.Users.Delete(u => u.Id == 1);
}
