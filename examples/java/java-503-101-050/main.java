@Target({ElementType.FIELD, ElementType.PARAMETER})
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = PasswordStrengthValidator.class)
public @interface StrongPassword {
    String message() default "Password must contain uppercase, lowercase, digit and special character";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
}

public class PasswordStrengthValidator 
    implements ConstraintValidator<StrongPassword, String> {
    
    private static final Pattern UPPERCASE = Pattern.compile("[A-Z]");
    private static final Pattern LOWERCASE = Pattern.compile("[a-z]");
    private static final Pattern DIGIT = Pattern.compile("[0-9]");
    private static final Pattern SPECIAL = Pattern.compile("[!@#$%^&*()_+\\-=\\[\\]{};':\"\\\\|,.<>\\/?]");
    
    @Override
    public boolean isValid(String password, ConstraintValidatorContext context) {
        if (password == null || password.isEmpty()) {
            return true; // null проверяется аннотацией @NotBlank
        }
        
        return UPPERCASE.matcher(password).find()
            && LOWERCASE.matcher(password).find()
            && DIGIT.matcher(password).find()
            && SPECIAL.matcher(password).find();
    }
}

// Использование
public class ChangePasswordRequest {
    @NotBlank
    @StrongPassword
    private String newPassword;
    
    // ...
}
