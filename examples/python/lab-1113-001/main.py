import pandas as pd

# 1. Таблица (из словаря, CSV или Excel)
df = pd.DataFrame({
    "name": ["Аня", "Боря", "Вера"],
    "score": [5, 4, 5],
})

# 2. Осмотр — что вообще загрузилось
print(df.head())
print(df.describe())

# 3. Операция (пример — средний балл класса)
print("Средний балл:", df["score"].mean())
