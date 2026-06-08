
import xgboost as xgb

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

# Создание DMatrix для эффективной работы с памятью
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

# Параметры модели
params = {
    'objective': 'binary:logistic',
    'max_depth': 6,
    'eta': 0.1,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'min_child_weight': 1,
    'eval_metric': 'logloss'
}

# Обучение модели
model = xgb.train(
    params,
    dtrain,
    num_boost_round=100,
    evals=[(dtest, 'eval')],
    early_stopping_rounds=10,
    verbose_eval=False
)

# Прогнозирование
predictions = model.predict(dtest)
