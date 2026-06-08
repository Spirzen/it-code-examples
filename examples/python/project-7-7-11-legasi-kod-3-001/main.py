# legacy_pricing.py
def legacy_price(base: int, is_vip: bool) -> int:
    if is_vip:
        return int(base * 0.9)  # исторически — округление вниз
    return base

# test_legacy_pricing.py
from legacy_pricing import legacy_price

def test_vip_price_matches_current_behavior():
    assert legacy_price(100, is_vip=True) == 90

def test_regular_unchanged():
    assert legacy_price(100, is_vip=False) == 100
