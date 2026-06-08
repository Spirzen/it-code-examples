// Потенциальное узкое место: O(n²)
foreach (var customer in customers)
{
    foreach (var order in orders)
    {
        if (order.CustomerId == customer.Id)
        {
            // Обработка
        }
    }
}
