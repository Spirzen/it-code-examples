import pandas as pd

df = pd.DataFrame({
    "region": ["Север", "Юг", "Север", "Юг", "Север"],
    "month": ["Jan", "Jan", "Feb", "Feb", "Feb"],
    "sales": [100, 80, 120, 90, 110],
})

pivot = df.pivot_table(
    values="sales",
    index="region",
    columns="month",
    aggfunc="sum",
    fill_value=0,
)

print(pivot)
