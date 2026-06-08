
import pickle

data = {
    "session_id": "abc123",
    "cart": ["book", "pen", "notebook"],
    "total": 1250.75
}

with open("session.pkl", "wb") as f:
    pickle.dump(data, f)

with open("session.pkl", "rb") as f:
    restored_data = pickle.load(f)

print("Восстановленные данные:", restored_data)
