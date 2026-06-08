
import pytest

from email_validator import validate_email, ValidationResult


@pytest.mark.parametrize("email", [
    "user@example.com",
    "test.email+tag@sub.domain.co.uk",
    "a@b.c",
])
def test_validate_valid_email_returns_success(email):
    # Act
    result = validate_email(email)
    # Assert
    assert result == ValidationResult(is_valid=True)


@pytest.mark.parametrize("email", [None, "", "   "])
def test_validate_null_or_whitespace_returns_empty_error(email):
    result = validate_email(email)
    assert result == ValidationResult(
        is_valid=False,
        error_message="Email не может быть пустым"
    )


@pytest.mark.parametrize("email", [
    "missing-at.com",
    "double@@example.com",
    "@domain.com",
])
def test_validate_invalid_at_count_returns_at_error(email):
    result = validate_email(email)
    assert result == ValidationResult(
        is_valid=False,
        error_message="Email должен содержать ровно один символ '@'"
    )


@pytest.mark.parametrize("email", [
    "user@",
    "user@.com",
    "user@com.",
    "user@com",  # без точки
])
def test_validate_invalid_domain_returns_domain_error(email):
    result = validate_email(email)
    assert result == ValidationResult(
        is_valid=False,
        error_message="Некорректный домен: должен содержать точку и не начинаться/заканчиваться ею"
    )


def test_validate_empty_local_part_returns_local_error():
    result = validate_email("@example.com")
    assert result == ValidationResult(
        is_valid=False,
        error_message="Локальная часть email не может быть пустой"
    )
