[ApiController]
[Route("api/v1/[controller]")]
public class TasksController : ControllerBase
{
    private readonly ITaskStore _store;

    public TasksController(ITaskStore store) => _store = store;

    [HttpGet]
    public ActionResult<IEnumerable<TaskDto>> GetAll([FromQuery] string? status)
    {
        var items = _store.GetAll(status).Select(Map);
        return Ok(items);
    }

    [HttpGet("{id:guid}")]
    public ActionResult<TaskDto> GetById(Guid id)
    {
        var item = _store.GetById(id);
        return item is null ? NotFound() : Ok(Map(item));
    }

    [HttpPost]
    public ActionResult<TaskDto> Create([FromBody] CreateTaskRequest request)
    {
        if (string.IsNullOrWhiteSpace(request.Title))
            return BadRequest(new { error = "Title is required" });

        var entity = new TaskItem
        {
            Title = request.Title.Trim(),
            Status = Enum.Parse<TaskStatus>(request.Status, ignoreCase: true)
        };
        _store.Add(entity);
        var dto = Map(entity);
        return CreatedAtAction(nameof(GetById), new { id = dto.Id }, dto);
    }

    [HttpPut("{id:guid}")]
    public ActionResult<TaskDto> Update(Guid id, [FromBody] UpdateTaskRequest request)
    {
        var existing = _store.GetById(id);
        if (existing is null) return NotFound();
        existing.Title = request.Title.Trim();
        existing.Status = Enum.Parse<TaskStatus>(request.Status, ignoreCase: true);
        _store.Update(existing);
        return Ok(Map(existing));
    }

    [HttpDelete("{id:guid}")]
    public IActionResult Delete(Guid id) =>
        _store.Delete(id) ? NoContent() : NotFound();

    private static TaskDto Map(TaskItem t) =>
        new(t.Id, t.Title, t.Status.ToString(), t.CreatedAt);
}
