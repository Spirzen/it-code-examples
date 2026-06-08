
import pytest

from logic import normalize_title


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("a", "a"),
        ("  b ", "b"),
        ("\tc\n", "c"),
    ],
)
def test_normalize_examples(raw, expected):
    assert normalize_title(raw) == expected
