// События
public record OrderCreated(Guid OrderId, string CustomerId, DateTime Timestamp);
public record OrderItemAdded(Guid OrderId, Product Product, int Quantity);
public record OrderCompleted(Guid OrderId, decimal TotalAmount);

// Агрегат
public class Order
{
    private readonly List<object> _events = new();
    public Guid Id { get; private set; }
    public string CustomerId { get; private set; }
    public List<OrderItem> Items { get; } = new();
    public bool IsCompleted { get; private set; }

    public void Create(string customerId)
    {
        var ev = new OrderCreated(Id, customerId, DateTime.UtcNow);
        Apply(ev);
        _events.Add(ev);
    }

    public void AddItem(Product product, int quantity)
    {
        var ev = new OrderItemAdded(Id, product, quantity);
        Apply(ev);
        _events.Add(ev);
    }

    public void Complete(decimal totalAmount)
    {
        var ev = new OrderCompleted(Id, totalAmount);
        Apply(ev);
        _events.Add(ev);
    }

    private void Apply(object ev)
    {
        switch (ev)
        {
            case OrderCreated created:
                Id = created.OrderId;
                CustomerId = created.CustomerId;
                break;
            case OrderItemAdded added:
                Items.Add(new OrderItem(added.Product, added.Quantity));
                break;
            case OrderCompleted _:
                IsCompleted = true;
                break;
        }
    }

    public IEnumerable<object> GetUncommittedEvents() => _events;
    public void ClearEvents() => _events.Clear();
}
