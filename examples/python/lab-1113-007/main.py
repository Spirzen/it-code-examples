import pandas as pd

df = pd.DataFrame({
    "city": ["Москва", "Казань", "Москва", "Казань", "Москва"],
    "product": ["A", "A", "B", "B", "A"],
    "amount": [100, 80, 120, 90, 150],
})

report = (
    df.groupby(["city", "product"], as_index=False)
    .agg(revenue=("amount", "sum"), orders=("amount", "count"))
    .sort_values("revenue", ascending=False)
)

print(report)
