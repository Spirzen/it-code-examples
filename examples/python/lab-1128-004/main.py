def print_permutations(a: list[int], path: list[int] | None = None) -> None:
    if path is None:
        path = []
    if len(path) == len(a):
        print(path)
        return
    for x in a:
        if x in path:
            continue
        path.append(x)
        print_permutations(a, path)
        path.pop()

if __name__ == "__main__":
    print_permutations([1, 2, 3])
