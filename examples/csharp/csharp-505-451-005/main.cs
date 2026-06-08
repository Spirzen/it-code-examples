   public class LoggingMiddleware
   {
       private readonly RequestDelegate _next;
       
       public LoggingMiddleware(RequestDelegate next) // только transient/singleton
       {
           _next = next;
       }
       
       public async Task InvokeAsync(HttpContext context)
       {
           var logger = context.RequestServices.GetRequiredService<ILogger<LoggingMiddleware>>();
           logger.LogInformation("Request started");
           await _next(context);
       }
   }
