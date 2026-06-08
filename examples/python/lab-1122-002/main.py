def bin_search(a, target):
    lo, hi = 0, len(a) - 1      # границы текущего диапазона
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid           # нашли — индекс в Python (с 0)
        if a[mid] < target:
            lo = mid + 1         # ответ правее mid
        else:
            hi = mid - 1         # ответ левее mid
    return -1                    # не нашли

a = sorted(map(int, inputsplit()))
x = int(input())
idx = bin_search(a, x)
print(idx + 1 if idx >= 0 else 0)   # перевод в 1-based, если так в условии
