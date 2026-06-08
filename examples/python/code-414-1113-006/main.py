
import sqlite3
import pickle
import random

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # SQL-инъекция
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()

def load_session(data):
    # Небезопасная десериализация
    return pickle.loads(data)

def generate_token():
    # Предсказуемый генератор
    return "".join(random.choice("abcdef0123456789") for _ in range(32))
