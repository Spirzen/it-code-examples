import pandas as pd

df = pd.DataFrame({
    "code": ["SKU-1001", "SKU-2042", "ITEM-99", "sku-3000"],
    "note": ["  срочно  ", "обычный", None, "  VIP "],
})

mask = df["code"].str.contains("SKU", case=False, na=False)
nums = df["code"].str.extract(r"(\d+)", expand=False)
df["note"] = df["note"].str.strip().str.upper()

print("Строки с SKU:\n", df[mask])
print("\nИзвлечённые номера:\n", nums)
print("\nПримечания:\n", df["note"])
