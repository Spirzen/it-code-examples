@RestController
@RequestMapping("/api/todos")
public class TodoController {
  private final TodoService service;

  public TodoController(TodoService service) {
    this.service = service;
  }

  @GetMapping
  public List<Todo> list() {
    return service.findAll();
  }
}
