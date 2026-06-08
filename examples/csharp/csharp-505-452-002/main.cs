public class TimingMiddleware
{
    private readonly RequestDelegate _next;

    public TimingMiddleware(RequestDelegate next) => _next = next;

    public async Task InvokeAsync(HttpContext context, ILogger<TimingMiddleware> logger)
    {
        var start = DateTime.UtcNow;
        await _next(context);
        var elapsed = DateTime.UtcNow - start;
        logger.LogInformation("Request {Path} took {Elapsed} ms", context.Request.Path, elapsed.TotalMilliseconds);
    }
}

// Регистрация:
app.UseMiddleware<TimingMiddleware>();
