def two_sum_slow(a: list[int], k: int) -> bool:
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == k:
                return True
    return False

def two_sum_fast(a: list[int], k: int) -> bool:
    seen: set[int] = set()
    for x in a:
        if k - x in seen:
            return True
        seen.add(x)
    return False

if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    print(two_sum_slow(arr, 9))   # True  (2+7)
    print(two_sum_fast(arr, 9))   # True
