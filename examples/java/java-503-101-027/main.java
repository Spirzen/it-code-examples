@Service
public class UserService {
    private final PasswordEncoder passwordEncoder;
    
    public User register(String email, String password) {
        // Хеширование пароля
        String hashedPassword = passwordEncoder.encode(password);
        
        User user = new User();
        user.setEmail(email);
        user.setPasswordHash(hashedPassword);
        user.setCreatedAt(LocalDateTime.now());
        
        return userRepository.save(user);
    }
    
    public boolean authenticate(String email, String password) {
        User user = userRepository.findByEmail(email)
            .orElseThrow(() -> new AuthenticationException("User not found"));
        
        // Сравнение хешей
        return passwordEncoder.matches(password, user.getPasswordHash());
    }
}
