import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, LabelEncoder

df = pd.DataFrame({
    "color": ["Green", "Red", "Black", "Green"],
    "size": ["XS", "S", "L", "M"],
})

# One-hot (dummy — drop_first=True)
color_ohe = pd.get_dummies(df["color"], prefix="color")
# drop_first=True даёт dummy encoding

# Ordinal — порядок задаём явно
size_ord = OrdinalEncoder(categories=[["XS", "S", "M", "L"]])
df["size_ord"] = size_ord.fit_transform(df[["size"]])

# Label — одна колонка целых
le = LabelEncoder()
df["color_label"] = le.fit_transform(df["color"])

# Count — только по train; здесь иллюстрация на всём df
counts = df["color"].value_counts()
df["color_count"] = df["color"].map(counts)
