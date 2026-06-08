using MinimalNotes.Models;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(options =>
{
    options.SwaggerDoc("v1", new() { Title = "Minimal Notes API", Version = "v1" });
});

var notes = new List<Note>();
var nextId = 1;

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

var api = app.MapGroup("/api/notes")
    .WithTags("Notes");

api.MapGet("/", () => Results.Ok(notes.OrderByDescending(n => n.Created)));

api.MapPost("/", (CreateNoteRequest req) =>
{
    if (string.IsNullOrWhiteSpace(req.Text))
        return Results.ValidationProblem(new Dictionary<string, string[]>
        {
            ["Text"] = ["Текст обязателен"]
        });

    var note = new Note(nextId++, req.Text.Trim(), DateTime.UtcNow);
    notes.Add(note);
    return Results.Created($"/api/notes/{note.Id}", note);
});

api.MapGet("/{id:int}", (int id) =>
    notes.FirstOrDefault(n => n.Id == id) is { } note
        ? Results.Ok(note)
        : Results.NotFound());

api.MapDelete("/{id:int}", (int id) =>
{
    var idx = notes.FindIndex(n => n.Id == id);
    if (idx < 0) return Results.NotFound();
    notes.RemoveAt(idx);
    return Results.NoContent();
});

app.Run();

public partial class Program { }
