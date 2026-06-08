from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

num_cols = ["Rooms", "Distance", "Bedroom2", "Bathroom", "Car",
            "Landsize", "BuildingArea", "YearBuilt"]
cat_cols = ["Suburb", "CouncilArea", "Type"]

preprocess = ColumnTransformer([
    ("num", SimpleImputer(strategy="median"), num_cols),
    ("cat", Pipeline([
        ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ]), cat_cols),
])

pipe = Pipeline([
    ("prep", preprocess),
    ("model", ensemble.GradientBoostingRegressor(random_state=42)),
])
pipe.fit(df[num_cols + cat_cols], df["Price"])
