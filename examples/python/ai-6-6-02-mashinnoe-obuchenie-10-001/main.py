from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2.0, 4.1, 5.0, 4.2, 5.1])

model = LinearRegression()
model.fit(X, y)
pred = model.predict([[6]])

print(pred[0], model.coef_, model.intercept_)
print("MAE:", mean_absolute_error(y, model.predict(X)))
print("R²:", r2_score(y, model.predict(X)))
