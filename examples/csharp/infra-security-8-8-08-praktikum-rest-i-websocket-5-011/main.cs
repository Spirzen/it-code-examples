var app = builder.Build();

app.UseAuthentication();
app.UseAuthorization();

app.MapPost("/api/v1/auth/token", (LoginRequest req, IConfiguration cfg) =>
{
    // учебный логин: demo / demo
    if (req.Username != "demo" || req.Password != "demo")
        return Results.Unauthorized();
    var token = JwtHelper.IssueToken(req.Username, cfg);
    return Results.Ok(new { access_token = token, token_type = "Bearer", expires_in = 3600 });
});

var orders = app.MapGroup("/api/v1/orders").RequireAuthorization();

orders.MapGet("/", async (HttpContext ctx, OrderService svc) =>
{
    var userId = ctx.User.Identity!.Name!;
    var list = await svc.ListForUserAsync(userId);
    return Results.Ok(list.Select(OrderMapper.ToResponse));
});

orders.MapPost("/", async (CreateOrderRequest body, HttpContext ctx, OrderService svc, CancellationToken ct) =>
{
    try
    {
        var order = await svc.CreateOrderAsync(ctx.User.Identity!.Name!, body, ct);
        return Results.Created($"/api/v1/orders/{order.Id}", OrderMapper.ToResponse(order));
    }
    catch (InsufficientStockException ex)
    {
        return Results.Conflict(new { title = ex.Message });
    }
    catch (HttpRequestException)
    {
        return Results.Json(new { title = "Catalog unavailable" }, statusCode: 502);
    }
});

app.Run("http://localhost:5200");
