using Microsoft.AspNetCore.Mvc;

namespace HelloApi.Controllers;

[ApiController]
[Route("api/[controller]")]
public class NotesController : ControllerBase
{
    private static readonly List<Note> Notes = new();

    [HttpGet]
    public ActionResult<IEnumerable<Note>> GetAll() => Ok(Notes);

    [HttpPost]
    public ActionResult<Note> Create(NoteCreate dto)
    {
        var note = new Note { Id = Notes.Count + 1, Text = dto.Text };
        Notes.Add(note);
        return CreatedAtAction(nameof(GetAll), new { id = note.Id }, note);
    }
}

public record Note(int Id, string Text);
public record NoteCreate(string Text);
