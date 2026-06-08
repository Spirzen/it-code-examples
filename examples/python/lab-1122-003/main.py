a = list(map(int, inputsplit()))
b = list(map(int, inputsplit()))
i = j = 0
merged = []
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1
merged.extend(a[i:])    # хвост того списка, который не закончился
merged.extend(b[j:])
print(*merged)
