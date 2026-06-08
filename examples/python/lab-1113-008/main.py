import pandas as pd
import numpy as np

raw = pd.DataFrame({
    "email": ["a@mail.ru", "A@mail.ru", "b@mail.ru", None, "c@mail.ru"],
    "answer": [" Да ", "да", "Нет", "Да", "нет"],
    "age": [17, 17, 16, np.nan, 18],
})

clean = (
    raw.dropna(subset=["email"])
    .assign(
        email=lambda x: x["email"].str.lower().str.strip(),
        answer=lambda x: x["answer"].str.strip().str.capitalize(),
        age=lambda x: x["age"].fillna(x["age"].median()),
    )
    .drop_duplicates(subset=["email"], keep="first")
)

print("Было строк:", len(raw), "→ стало:", len(clean))
print(clean)
