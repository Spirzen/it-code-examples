var app = builder.Build();

// GET с параметром из маршрута
app.MapGet("/users/{id:int}", (int id) => Results.Ok(new { Id = id, Name = "Timur" }));

// POST с телом (автопривязка)
app.MapPost("/users", (User user) => {
    // ModelState.IsValid — недоступен напрямую!
    // Нужно: 
    //   var http = httpContextAccessor.HttpContext!;
    //   if (!http.RequestServices.GetRequiredService<IModelValidator>().Validate(...))
    return Results.Created($"/users/{user.Id}", user);
});

// DI в параметрах
app.MapGet("/time", (TimeProvider time) => Results.Ok(time.GetUtcNow()));
