from catboost import CatBoostClassifier, Pool

import pandas as pd

# Создание данных с категориальными признаками
df = pd.DataFrame({
    'age': [25, 32, 47, 51, 35],
    'city': ['Moscow', 'SPB', 'Moscow', 'Kazan', 'SPB'],
    'income': [50000, 70000, 90000, 120000, 80000],
    'target': [0, 1, 1, 1, 0]
})

# Указание категориальных признаков
cat_features = ['city']

# Создание пула данных
train_pool = Pool(
    data=df[['age', 'city', 'income']],
    label=df['target'],
    cat_features=cat_features
)

# Обучение модели
model = CatBoostClassifier(
    iterations=100,
    learning_rate=0.1,
    depth=6,
    loss_function='Logloss',
    verbose=False
)
model.fit(train_pool)
