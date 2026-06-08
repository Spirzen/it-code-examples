from discount import get_discount_percent


def test_discount_for_small_order():
    assert get_discount_percent(900) == 0


def test_discount_for_medium_order():
    assert get_discount_percent(1500) == 5


def test_discount_for_large_order():
    assert get_discount_percent(6000) == 10
