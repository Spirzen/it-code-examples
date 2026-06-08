@Service
@Transactional
public class UserService {
    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public User register(String email, String name) {
        User user = new User();
        user.setEmail(email);
        user.setName(name);
        user.setStatus(Status.PENDING);
        return userRepository.save(user); // вставляет или обновляет
    }
}
