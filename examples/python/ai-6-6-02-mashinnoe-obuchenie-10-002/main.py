from sklearn.model_selection import GridSearchCV

param_grid = {
    "clf__C": [0.1, 1, 10],
    "clf__gamma": ["scale", "auto"],
}

search = GridSearchCV(
    pipe,
    param_grid,
    cv=5,
    scoring="f1_macro",
    n_jobs=-1,
)
search.fit(X_train, y_train)
print(search.best_params_, search.best_score_)
print("Test:", search.score(X_test, y_test))
