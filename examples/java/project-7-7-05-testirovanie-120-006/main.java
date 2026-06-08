
import java.util.Objects;

public final class EmailValidator {

    public static final class ValidationResult {
        private final boolean isValid;
        private final String errorMessage;

        private ValidationResult(boolean isValid, String errorMessage) {
            this.isValid = isValid;
            this.errorMessage = errorMessage;
        }

        public static ValidationResult success() {
            return new ValidationResult(true, null);
        }

        public static ValidationResult error(String message) {
            return new ValidationResult(false, message);
        }

        public boolean isValid() { return isValid; }
        public String errorMessage() { return errorMessage; }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            ValidationResult that = (ValidationResult) o;
            return isValid == that.isValid &&
                   Objects.equals(errorMessage, that.errorMessage);
        }

        @Override
        public int hashCode() {
            return Objects.hash(isValid, errorMessage);
        }
    }

    public static ValidationResult validate(String email) {
        if (email == null || email.trim().isEmpty()) {
            return ValidationResult.error("Email не может быть пустым");
        }

        String[] parts = email.split("@", -1); // -1 сохраняет пустые части
        if (parts.length != 2) {
            return ValidationResult.error("Email должен содержать ровно один символ '@'");
        }

        String local = parts[0];
        String domain = parts[1];

        if (local.isEmpty()) {
            return ValidationResult.error("Локальная часть email не может быть пустой");
        }

        if (domain.isEmpty() || !domain.contains(".") ||
            domain.startsWith(".") || domain.endsWith(".")) {
            return ValidationResult.error("Некорректный домен: должен содержать точку и не начинаться/заканчиваться ею");
        }

        return ValidationResult.success();
    }
}
