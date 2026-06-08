public class UserController {
    
    public ResponseEntity<User> createUser(@RequestBody UserRequest request) {
        // Валидация
        if (request.getEmail() == null || !isValidEmail(request.getEmail())) {
            return ResponseEntity.badRequest().build();
        }
        
        if (request.getPassword() == null || request.getPassword().length() < 8) {
            return ResponseEntity.badRequest().build();
        }
        
        // Создание пользователя
        User user = userService.register(request.getEmail(), request.getPassword());
        return ResponseEntity.ok(user);
    }
    
    private boolean isValidEmail(String email) {
        return email != null && email.matches("^[A-Za-z0-9+_.-]+@(.+)$");
    }
}
