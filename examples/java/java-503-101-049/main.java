public class UserRegistrationRequest {
    @NotBlank(message = "Email required")
    @Email(message = "Invalid email format")
    @Size(max = 255)
    private String email;
    
    @NotBlank(message = "Password required")
    @Size(min = 8, max = 128, message = "Password must be 8-128 characters")
    private String password;
    
    @Pattern(regexp = "^[A-Za-zа-яА-ЯёЁ\\s-]+$", message = "Invalid name format")
    @Size(min = 2, max = 100)
    private String firstName;
    
    @Size(max = 100)
    private String lastName;
    
    @NotNull(message = "Birth date required")
    @Past(message = "Birth date must be in the past")
    private LocalDate birthDate;
    
    // геттеры и сеттеры
}

@RestController
public class UserController {
    @PostMapping("/users")
    public ResponseEntity<UserResponse> register(
        @Valid @RequestBody UserRegistrationRequest request
    ) {
        // обработка валидного запроса
    }
    
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidationErrors(
        MethodArgumentNotValidException ex
    ) {
        List<String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .map(error -> error.getField() + ": " + error.getDefaultMessage())
            .collect(Collectors.toList());
        
        return ResponseEntity.badRequest()
            .body(new ErrorResponse("VALIDATION_ERROR", errors));
    }
}
