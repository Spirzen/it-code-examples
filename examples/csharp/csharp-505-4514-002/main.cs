using System.ComponentModel.DataAnnotations;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using NotesRazor.Services;

namespace NotesRazor.Pages.Notes;

public class IndexModel : PageModel
{
    private readonly NoteStore _store;

    public IndexModel(NoteStore store) => _store = store;

    public IReadOnlyList<Models.Note> Items { get; private set; } = [];

    [BindProperty]
    [Required(ErrorMessage = "Введите текст заметки")]
    [StringLength(500)]
    public string NewText { get; set; } = "";

    public void OnGet()
    {
        Items = _store.GetAll();
    }

    public IActionResult OnPost()
    {
        if (!ModelState.IsValid)
        {
            Items = _store.GetAll();
            return Page();
        }

        _store.Add(NewText);
        return RedirectToPage();
    }
}
