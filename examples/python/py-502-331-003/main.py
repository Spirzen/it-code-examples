
import pandas as pd

df = pd.read_csv("sales.csv")
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date", "amount"])
df["month"] = df["date"].dt.to_period("M").astype(str)

report = (
    df.groupby(["month", "region"], as_index=False)
      .agg(total_amount=("amount", "sum"), orders=("order_id", "nunique"))
      .sort_values(["month", "total_amount"], ascending=[True, False])
)

report.to_csv("sales_report.csv", index=False)
