from collections import defaultdict

n, m = map(int, inputsplit())   # n вершин, m рёбер
g = defaultdict(list)
for _ in range(m):
    u, v = map(int, inputsplit())
    g[u].append(v)
    g[v].append(u)                 # неориентированный граф

start = int(input())
stack = [start]
seen = {start}
order = []
while stack:
    v = stack.pop()                # LIFO — как рекурсивный DFS
    order.append(v)
    for to in sorted(g[v], reverse=True):
        if to not in seen:
            seen.add(to)
            stack.append(to)
print(*order)
