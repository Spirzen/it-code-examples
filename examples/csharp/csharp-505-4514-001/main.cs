using NotesRazor.Models;

namespace NotesRazor.Services;

public class NoteStore
{
    private readonly List<Note> _items = new();
    private int _nextId = 1;

    public IReadOnlyList<Note> GetAll() =>
        _items.OrderByDescending(n => n.Created).ToList();

    public void Add(string text)
    {
        _items.Add(new Note { Id = _nextId++, Text = text.Trim() });
    }
}
