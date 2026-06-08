
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def fetch_user(self, user_id):
        # Имитация запроса к БД
        # В реальности здесь был бы SQL запрос
        if user_id == 1:
            return {"id": 1, "name": "Alice"}
        return None

def get_user_data(user_id):
    db = DatabaseConnection("users.db")
    data = db.fetch_user(user_id)
    if data is None:
        raise ValueError(f"User {user_id} not found")
    return data["name"]
