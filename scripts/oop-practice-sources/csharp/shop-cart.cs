class Product
{
    public string Name { get; }
    public int Price { get; }

    public Product(string name, int price)
    {
        Name = name;
        Price = price;
    }
}

class Cart
{
    public List<Product> Items { get; } = new();

    public void Add(Product product)
    {
        Items.Add(product);
        Console.WriteLine($"В корзину добавлено: {product.Name} ({product.Price} ₽)");
    }

    public int Total()
    {
        return Items.Sum(p => p.Price);
    }
}

class Order
{
    public List<Product> Items { get; }
    public int Total { get; }

    public Order(Cart cart)
    {
        Items = new List<Product>(cart.Items);
        Total = cart.Total();
    }

    public void Checkout()
    {
        Console.WriteLine("Оформление заказа...");
        foreach (var item in Items)
        {
            Console.WriteLine($"  — {item.Name}: {item.Price} ₽");
        }
        Console.WriteLine($"Итого: {Total} ₽");
        Console.WriteLine("Заказ оформлен!");
    }
}

class Program
{
    static void Main()
    {
        var cart = new Cart();
        cart.Add(new Product("Книга", 500));
        cart.Add(new Product("Ручка", 50));
        var order = new Order(cart);
        order.Checkout();
    }
}
