base = ensemble.GradientBoostingRegressor(random_state=42)
param_grid = {
    "n_estimators": [200, 300],
    "max_depth": [4, 6],
    "min_samples_split": [3, 4],
    "min_samples_leaf": [5, 6],
    "learning_rate": [0.01, 0.1],
    "max_features": [0.8, 0.9],
    "loss": ["huber", "squared_error"],
}

grid = GridSearchCV(base, param_grid, n_jobs=-1, cv=3, scoring="neg_mean_absolute_error")
grid.fit(X_train, y_train)
print(grid.best_params_)

best = grid.best_estimator_
print("MAE test:", mean_absolute_error(y_test, best.predict(X_test)))
