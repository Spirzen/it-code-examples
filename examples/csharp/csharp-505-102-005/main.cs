// Фабричный метод для создания объекта с валидацией
public static Order CreateNew(Customer customer, DateTime orderDate)
{
    if (customer == null)
        throw new ArgumentNullException(nameof(customer));
    
    if (orderDate > DateTime.UtcNow)
        throw new ArgumentException("Order date cannot be in the future", nameof(orderDate));
    
    return new Order
    {
        Customer = customer,
        OrderDate = orderDate,
        Status = OrderStatus.Pending,
        Items = new List<OrderItem>()
    };
}
