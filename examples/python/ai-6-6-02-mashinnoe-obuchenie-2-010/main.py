
import lightgbm as lgb

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Генерация данных
X, y = make_classification(
    n_samples=10000,
    n_features=50,
    n_informative=30,
    n_redundant=20,
    random_state=42
)

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Создание датасета LightGBM
train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test, reference=train_data)

# Параметры модели
params = {
    'objective': 'binary',
    'metric': 'binary_logloss',
    'max_depth': 6,
    'learning_rate': 0.1,
    'num_leaves': 31,
    'feature_fraction': 0.8,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'min_child_samples': 20
}

# Обучение модели
model = lgb.train(
    params,
    train_data,
    num_boost_round=100,
    valid_sets=[test_data],
    callbacks=[lgb.early_stopping(stopping_rounds=10)]
)

# Прогнозирование
predictions = model.predict(X_test)
