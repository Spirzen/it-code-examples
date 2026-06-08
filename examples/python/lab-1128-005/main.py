from collections import deque

def bad_queue(n: int) -> int:
    q = list(range(n))
    s = 0
    while q:
        s += q.pop(0)
    return s

def good_queue(n: int) -> int:
    q = deque(range(n))
    s = 0
    while q:
        s += q.popleft()
    return s
