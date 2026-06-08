// Плохо: двунаправленная зависимость
public class Order
{
    public Customer Customer { get; set; }
}

public class Customer
{
    public List<Order> Orders { get; set; }
}

// Хорошо: зависимость через интерфейс
public interface IOrderRepository
{
    IEnumerable<Order> GetOrdersForCustomer(Customer customer);
}

public class CustomerService
{
    private readonly IOrderRepository _orderRepository;
    
    public CustomerService(IOrderRepository orderRepository)
    {
        _orderRepository = orderRepository;
    }
    
    public IEnumerable<Order> GetCustomerOrders(Customer customer)
    {
        return _orderRepository.GetOrdersForCustomer(customer);
    }
}
