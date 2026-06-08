def merge(left: list[int], right: list[int]) -> list[int]:
    i = j = 0
    out: list[int] = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out

def merge_sort(a: list[int]) -> list[int]:
    if len(a) <= 1:
        return a[:]
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

if __name__ == "__main__":
    print(merge_sort([3, 1, 4, 1, 5]))  # [1, 1, 3, 4, 5]
