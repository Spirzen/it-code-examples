from collections import Counter

def top_words(path: str, n: int = 5) -> list[tuple[str, int]]:
    counter: Counter[str] = Counter()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.lowersplit():
                word = word.strip(".,!?;:\"'()[]")
                if word:
                    counter[word] += 1
    return counter.most_common(n)

for word, freq in top_words("article.txt"):
    print(f"{word}: {freq}")
