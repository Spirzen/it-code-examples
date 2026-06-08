import pandas as pd

df = pd.DataFrame({
    "name": ["Аня", "Боря", "Вера", "Глеб"],
    "class": ["10А", "10Б", "10А", "10Б"],
    "score": [5, 3, 4, 5],
})

top = df[df["score"] >= 4]
class_10a = df[df["class"] == "10А"]
both = df[(df["class"] == "10А") & (df["score"] == 5)]
by_list = df[df["name"].isin(["Аня", "Глеб"])]

print("Оценка 4 и выше:\n", top)
print("\n10А с пятёркой:\n", both)
