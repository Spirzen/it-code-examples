public async Task<Order> CreateOrderAsync(string userId, CreateOrderRequest request, CancellationToken ct)
{
    if (request.Lines.Count == 0)
        throw new ValidationException("Order must contain at least one line");

    var order = new Order
    {
        Id = $"ord_{Guid.NewGuid():N}"[..12],
        UserId = userId,
        Status = OrderStatus.Draft,
        CreatedAt = DateTimeOffset.UtcNow,
    };

    foreach (var line in request.Lines)
    {
        var product = await _catalog.GetProductAsync(line.ProductId, ct)
            ?? throw new ValidationException($"Unknown product {line.ProductId}");

        var reservation = await _catalog.ReserveAsync(
            line.ProductId,
            line.Quantity,
            order.Id,
            idempotencyKey: $"{order.Id}:{line.ProductId}",
            ct);

        order.Lines.Add(new OrderLine
        {
            ProductId = line.ProductId,
            Quantity = line.Quantity,
            UnitPrice = product.Price,
            ReservationId = reservation.ReservationId,
        });
    }

    order.Status = OrderStatus.Reserved;
    order.Total = order.Lines.Sum(l => l.UnitPrice * l.Quantity);
    _db.Orders.Add(order);
    await _db.SaveChangesAsync(ct);
    await _events.PublishAsync(new OrderStatusEvent(order.Id, order.Status.ToString()));
    return order;
}
