@Service
public class TodoService {
  private final TodoRepository repository;

  public TodoService(TodoRepository repository) {
    this.repository = repository;
  }

  public List<Todo> findAll() {
    return repository.findAll();
  }
}
