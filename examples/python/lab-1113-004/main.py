import pandas as pd
import numpy as np

df = pd.DataFrame({
    "id": [1, 2, 2, 3],
    "name": [" Аня ", "Боря", None, "Вера"],
    "score": [5, 4, 4, np.nan],
})

df["name"] = df["name"].str.strip()
df["score"] = df["score"].fillna(df["score"].median())
df = df.drop_duplicates(subset=["id"], keep="first")
df = df.dropna(subset=["name"])

print(df)
