
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import static org.assertj.core.api.Assertions.*;

class EmailValidatorTest {

    @ParameterizedTest
    @ValueSource(strings = {
        "user@example.com",
        "test.email+tag@sub.domain.co.uk",
        "a@b.c"
    })
    void validate_validEmail_returnsSuccess(String email) {
        var result = EmailValidator.validate(email);
        assertThat(result).isEqualTo(EmailValidator.ValidationResult.success());
    }

    @ParameterizedTest
    @ValueSource(strings = {"", "   "})
    void validate_emptyOrWhitespace_returnsEmptyError(String email) {
        var result = EmailValidator.validate(email);
        var expected = EmailValidator.ValidationResult.error("Email не может быть пустым");
        assertThat(result).isEqualTo(expected);
    }

    @Test
    void validate_nullInput_returnsEmptyError() {
        var result = EmailValidator.validate(null);
        var expected = EmailValidator.ValidationResult.error("Email не может быть пустым");
        assertThat(result).isEqualTo(expected);
    }

    @ParameterizedTest
    @ValueSource(strings = {
        "missing-at.com",
        "double@@example.com",
        "@domain.com"
    })
    void validate_invalidAtCount_returnsAtError(String email) {
        var result = EmailValidator.validate(email);
        var expected = EmailValidator.ValidationResult.error(
            "Email должен содержать ровно один символ '@'"
        );
        assertThat(result).isEqualTo(expected);
    }

    @ParameterizedTest
    @ValueSource(strings = {
        "user@",
        "user@.com",
        "user@com.",
        "user@com"
    })
    void validate_invalidDomain_returnsDomainError(String email) {
        var result = EmailValidator.validate(email);
        var expected = EmailValidator.ValidationResult.error(
            "Некорректный домен: должен содержать точку и не начинаться/заканчиваться ею"
        );
        assertThat(result).isEqualTo(expected);
    }

    @Test
    void validate_emptyLocalPart_returnsLocalError() {
        var result = EmailValidator.validate("@example.com");
        var expected = EmailValidator.ValidationResult.error(
            "Локальная часть email не может быть пустой"
        );
        assertThat(result).isEqualTo(expected);
    }
}
