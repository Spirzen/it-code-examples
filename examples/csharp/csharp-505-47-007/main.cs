// Program.cs
app.UseExceptionHandler(errorApp =>
{
    errorApp.Run(async context =>
    {
        context.Response.StatusCode = 500;
        context.Response.ContentType = "application/json";

        var exceptionHandlerPathFeature = 
            context.Features.Get<IExceptionHandlerPathFeature>();

        var logger = context.RequestServices.GetRequiredService<ILogger<Program>>();
        logger.LogError(exceptionHandlerPathFeature?.Error, "Произошла внутренняя ошибка");

        await context.Response.WriteAsync(JsonSerializer.Serialize(new
        {
            error = "Внутренняя ошибка сервера",
            path = exceptionHandlerPathFeature?.Path
        }));
    });
});
