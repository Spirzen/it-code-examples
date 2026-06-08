  // Команда
  public record CreateUserCommand(String email, String name) {}
  @Service
  public class UserCommandService {
      public void handle(CreateUserCommand cmd) {
          userRepository.save(new User(cmd.email(), cmd.name()));
      }
  }

  // Запрос
  public record GetUserQuery(Long id) {}
  @Service
  public class UserQueryService {
      public UserDto handle(GetUserQuery query) {
          return userRepository.findById(query.id())
              .map(u -> new UserDto(u.id(), u.email()))
              .orElseThrow();
      }
  }
