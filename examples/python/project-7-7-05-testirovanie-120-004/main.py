from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class ValidationResult:
    is_valid: bool
    error_message: Optional[str] = None

def validate_email(email: Optional[str]) -> ValidationResult:
    if not email or not email.strip():
        return ValidationResult(is_valid=False, error_message="Email не может быть пустым")

    parts = email.split('@')
    if len(parts) != 2:
        return ValidationResult(
            is_valid=False,
            error_message="Email должен содержать ровно один символ '@'"
        )

    local, domain = parts

    if not local:
        return ValidationResult(
            is_valid=False,
            error_message="Локальная часть email не может быть пустой"
        )

    if not domain or '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        return ValidationResult(
            is_valid=False,
            error_message="Некорректный домен: должен содержать точку и не начинаться/заканчиваться ею"
        )

    return ValidationResult(is_valid=True)
