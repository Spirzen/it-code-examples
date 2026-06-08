@RestController
@RequestMapping("/api/users")
public class UserController {

    @GetMapping("/{id}")
    public UserDto getById(@PathVariable Long id) {
        return new UserDto(id, "Alex");
    }

    @PostMapping
    public UserDto create(@RequestBody CreateUserRequest request) {
        return new UserDto(1L, request.name());
    }

    @GetMapping
    public List<UserDto> search(@RequestParam(defaultValue = "0") int page) {
        return List.of(new UserDto(1L, "Alex"));
    }
}
