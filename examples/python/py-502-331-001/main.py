sales = pd.DataFrame({
    "region": ["Север", "Север", "Юг", "Юг"],
    "product": ["A", "B", "A", "B"],
    "revenue": [100, 80, 120, 90],
})

pd.pivot_table(
    sales,
    values="revenue",
    index="region",
    columns="product",
    aggfunc="sum",
    fill_value=0,
)
