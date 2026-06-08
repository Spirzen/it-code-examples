
import pandas as pd
import numpy as np

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Создание временного ряда с несколькими сезонностями
np.random.seed(42)
date_range = pd.date_range(start='2022-01-01', periods=1000, freq='H')
hourly_pattern = 10 * np.sin(2 * np.pi * np.arange(1000) / 24)
daily_pattern = 15 * np.sin(2 * np.pi * np.arange(1000) / (24 * 7))
trend = np.linspace(0, 30, 1000)
noise = np.random.normal(0, 3, 1000)
values = hourly_pattern + daily_pattern + trend + noise

df = pd.DataFrame({'timestamp': date_range, 'value': values})

# Создание признаков для временного ряда
def create_time_features(df, target_col='value', max_lag=48):
    df = df.copy()
    
    # Лаговые признаки
    for lag in range(1, max_lag + 1):
        df[f'lag_{lag}'] = df[target_col].shift(lag)
    
    # Скользящие статистики
    for window in [6, 12, 24]:
        df[f'rolling_mean_{window}'] = df[target_col].shift(1).rolling(window=window).mean()
        df[f'rolling_std_{window}'] = df[target_col].shift(1).rolling(window=window).std()
    
    # Временные признаки
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    
    # Удаление строк с пропущенными значениями из-за лагов
    df = df.dropna()
    return df

# Подготовка данных
df_features = create_time_features(df)
feature_cols = [col for col in df_features.columns if col not in ['timestamp', 'value']]

# Хронологическое разделение
split_idx = int(len(df_features) * 0.8)
train_df = df_features[:split_idx]
test_df = df_features[split_idx:]

X_train = train_df[feature_cols]
y_train = train_df['value']
X_test = test_df[feature_cols]
y_test = test_df['value']

# Создание и обучение модели
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('gbr', GradientBoostingRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=6,
        min_samples_split=10,
        min_samples_leaf=5,
        subsample=0.8,
        random_state=42
    ))
])

pipeline.fit(X_train, y_train)

# Прогнозирование и оценка
y_pred = pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"MAE на тесте: {mae:.2f}")
print(f"RMSE на тесте: {rmse:.2f}")

# Анализ важности признаков
feature_importance = pipeline.named_steps['gbr'].feature_importances_
importance_df = pd.DataFrame({
    'feature': feature_cols,
    'importance': feature_importance
}).sort_values('importance', ascending=False)

print("\nТоп-10 важных признаков:")
print(importance_df.head(10))
