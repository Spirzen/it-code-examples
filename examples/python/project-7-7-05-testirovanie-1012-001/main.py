
import psycopg2

from datetime import datetime

def connect_to_db():
    return psycopg2.connect(
        host="localhost",
        database="test_db",
        user="test_user",
        password="test_password"
    )

def save_user(name, email):
    conn = connect_to_db()
    try:
        cursor = conn.cursor()
        insert_query = """
            INSERT INTO users (name, email) 
            VALUES (%s, %s) RETURNING id;
        """
        cursor.execute(insert_query, (name, email))
        conn.commit()
        user_id = cursor.fetchone()[0]
        return user_id
    finally:
        conn.close()

def get_user(user_id):
    conn = connect_to_db()
    try:
        cursor = conn.cursor()
        select_query = "SELECT id, name, email FROM users WHERE id = %s;"
        cursor.execute(select_query, (user_id,))
        result = cursor.fetchone()
        if result:
            return {"id": result[0], "name": result[1], "email": result[2]}
        return None
    finally:
        conn.close()

def compare_fields(expected, actual):
    if expected["name"] != actual["name"]:
        raise ValueError("Имя не совпадает")
    if expected["email"] != actual["email"]:
        raise ValueError("Email не совпадает")
    return True
