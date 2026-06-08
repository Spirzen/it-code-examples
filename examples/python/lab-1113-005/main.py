import pandas as pd

orders = pd.DataFrame({
    "order_id": [1, 2, 3],
    "user_id": [10, 10, 20],
    "total": [500, 300, 1200],
})

users = pd.DataFrame({
    "user_id": [10, 20, 30],
    "name": ["Аня", "Боря", "Вера"],
})

result = orders.merge(users, on="user_id", how="left")
print(result)
