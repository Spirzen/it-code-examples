import pandas as pd

df = pd.DataFrame({
    "date": ["2024-01-05", "2024-01-20", "2024-02-10", "2024-02-28"],
    "sales": [100, 150, 200, 180],
})

df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")

monthly = df["sales"].resample("ME").sum()
rolling_avg = df["sales"].rolling(window=2, min_periods=1).mean()

print("По месяцам:\n", monthly)
print("\nСкользящее среднее (2 точки):\n", rolling_avg)
