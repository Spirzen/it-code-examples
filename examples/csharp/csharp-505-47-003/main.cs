// Pages/Products/Details.cshtml.cs
public class DetailsModel : PageModel
{
    private readonly AppDbContext _context;

    public DetailsModel(AppDbContext context) => _context = context;

    public Product? Product { get; set; }

    public async Task<IActionResult> OnGetAsync(int id)
    {
        Product = await _context.Products.FindAsync(id);
        if (Product == null) return NotFound();
        return Page();
    }
}
