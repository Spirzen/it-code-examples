
import pytest

from validators import is_adult  # допустимый возраст: 18–99 включительно

@pytest.mark.parametrize("age,expected", [
    (17, False),   # ниже минимума
    (18, True),    # на нижней границе
    (25, True),    # середина валидного класса
    (99, True),    # на верхней границе
    (100, False),  # выше максимума
])
def test_is_adult_boundaries(age, expected):
    assert is_adult(age) == expected
