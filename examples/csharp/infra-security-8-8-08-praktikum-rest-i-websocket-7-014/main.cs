app.UseWebSockets();

app.Map("/ws/orders", async (HttpContext ctx, OrderWebSocketHub hub) =>
{
    if (!ctx.WebSockets.IsWebSocketRequest)
    {
        ctx.Response.StatusCode = 400;
        return;
    }
    if (ctx.User?.Identity?.IsAuthenticated != true)
    {
        ctx.Response.StatusCode = 401;
        return;
    }
    var socket = await ctx.WebSockets.AcceptWebSocketAsync();
    await hub.HandleAsync(socket, ctx.User.Identity!.Name!, ctx.RequestAborted);
});
