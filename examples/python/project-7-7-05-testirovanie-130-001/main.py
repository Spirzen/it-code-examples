def discount(total, is_vip):
    if total > 1000:
        rate = 0.1 if is_vip else 0.05
    else:
        rate = 0
    return total * rate

# Плохо: вызвали функцию, не проверили return
def test_discount_smoke():
    discount(1500, True)  # нет assert

# Хорошо
def test_vip_branch():
    assert discount(1500, True) == 150.0
