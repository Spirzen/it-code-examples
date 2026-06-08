[ApiController]
[Route("api/[controller]")]
public class AiAssistantController : ControllerBase
{
    private readonly IAiService _aiService;

    public AiAssistantController(IAiService aiService)
    {
        _aiService = aiService;
    }

    [HttpPost("summarize")]
    public async Task<IActionResult> Summarize([FromBody] SummarizeRequest request)
    {
        var summary = await _aiService.GenerateSummaryAsync(request.Text);
        return Ok(new { Summary = summary });
    }
}
