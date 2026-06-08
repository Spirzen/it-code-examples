using (var db = new AppDbContext()) {
    // Добавление
    var product = new Product { Name = "Laptop", Price = 1200 };
    db.Products.Add(product);
    db.SaveChanges();

    // Запрос
    var expensiveProducts = db.Products.Where(p => p.Price > 1000).ToList();

    // Обновление
    product.Price = 1100;
    db.SaveChanges();

    // Удаление
    db.Products.Remove(product);
    db.SaveChanges();
}
