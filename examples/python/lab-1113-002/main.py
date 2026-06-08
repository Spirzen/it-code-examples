import pandas as pd

df = pd.DataFrame({
    "city": ["Москва", "Казань", "Москва", "Сочи"],
    "product": ["A", "B", "A", "C"],
    "amount": [1200, 800, None, 1500],
    "qty": [2, 1, 3, 2],
})

print("Первые строки:\n", df.head(3))
print("\nСтруктура:\n")
df.info()
print("\nСтатистика:\n", df.describe())
print("\nПропуски по столбцам:\n", df.isnull().sum())
