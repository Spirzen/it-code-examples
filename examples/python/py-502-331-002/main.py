df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
df = df.set_index("date").sort_index()

# срез по периоду
q1 = df.loc["2026-01":"2026-03"]

# ресемплинг — сумма по неделям
weekly = df["amount"].resample("W").sum()

# скользящее среднее за 7 дней
df["ma7"] = df["amount"].rolling(7).mean()

# сдвиг на период, регулярная сетка, формат в строку
df["amount"].shift(1)
df["amount"].asfreq("D", method="ffill")
df.index.strftime("%Y-%m-%d")
