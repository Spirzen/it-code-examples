string connectionString = "...";
using (DataContext db = new DataContext(connectionString)) {
    var customers = db.GetTable<Customer>();
    
    // Выборка
    var query = from c in customers
                where c.Name.StartsWith("A")
                select c;

    foreach (var c in query) {
        Console.WriteLine(c.Name);
    }

    // Добавление
    Customer newCustomer = new Customer { Name = "Alice" };
    customers.InsertOnSubmit(newCustomer);
    db.SubmitChanges();
}
