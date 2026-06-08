def solve_slow(queries: list[int], data: list[int]) -> list[str]:
    out = []
    for q in queries:
        found = False
        for x in data:
            if x == q:
                found = True
                break
        out.append("yes" if found else "no")
    return out

def solve_fast(queries: list[int], data: list[int]) -> list[str]:
    index = set(data)
    return ["yes" if q in index else "no" for q in queries]
