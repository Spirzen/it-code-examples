[ApiController]
[Route("api/[controller]")]
[Authorize]
public class NotesController : ControllerBase
{
    private static readonly List<string> Notes = new();

    [HttpGet]
    public IActionResult GetAll() => Ok(Notes);

    [HttpPost]
    public IActionResult Add([FromBody] string text)
    {
        Notes.Add(text);
        return Ok();
    }
}
