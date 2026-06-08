public sealed record OrderLineDto(
    string ProductId,
    int Quantity,
    decimal UnitPrice,
    string? ReservationId);

public sealed record OrderResponse(
    string Id,
    string Status,
    IReadOnlyList<OrderLineDto> Lines,
    decimal Total,
    DateTimeOffset CreatedAt);

public sealed record CreateOrderRequest(
    IReadOnlyList<CreateOrderLineRequest> Lines);

public sealed record CreateOrderLineRequest(string ProductId, int Quantity);
