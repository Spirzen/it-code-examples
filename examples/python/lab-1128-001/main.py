def binary_search(a: list[int], target: int) -> int:
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10]
    print(binary_search(arr, 8))   # 3
    print(binary_search(arr, 7))   # -1
