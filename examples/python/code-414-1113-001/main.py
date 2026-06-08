
import pytest

from calculator import divide

def test_divide_success():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_divide_floats():
    assert divide(7.5, 2.5) == 3.0
