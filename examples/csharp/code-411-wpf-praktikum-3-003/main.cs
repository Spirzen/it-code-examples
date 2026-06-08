var builder = WebApplication.CreateBuilder(args);

builder.Services.AddCors(options =>
{
    options.AddPolicy("TaskDeskClient", policy =>
        policy.WithOrigins("http://localhost:5000") // dev WPF через proxy или *
              .AllowAnyHeader()
              .AllowAnyMethod());
});

// ... AddControllers, Swagger, ITaskStore

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseCors("TaskDeskClient");
app.MapControllers();

app.Run();
