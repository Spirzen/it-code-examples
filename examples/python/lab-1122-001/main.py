a = list(map(int, inputsplit()))
n = len(a)
found = False
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if a[i] + a[j] + a[k] == 0:
                found = True
                break
        if found:
            break
    if found:
        break
print("yes" if found else "no")
