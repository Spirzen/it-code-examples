# Идея Дейкстры — очередь с приоритетом по текущему расстоянию
# Упрощённо — без восстановления пути и без всех вершин графа

import heapq

def dijkstra(graph, start):
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist.get(u, float("inf")):
            continue
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

# graph = {"A" — [("B", 1), ("C", 4)], "B": [("C", 2)], "C": []}
