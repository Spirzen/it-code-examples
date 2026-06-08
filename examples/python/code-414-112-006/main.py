# Контекстные менеджеры в Python

import psycopg2

from contextlib import contextmanager

@contextmanager
def get_db_connection():
    connection = psycopg2.connect(DSN)
    try:
        yield connection
    finally:
        connection.close()

@contextmanager
def get_cursor(connection):
    cursor = connection.cursor()
    try:
        yield cursor
    finally:
        cursor.close()

def fetch_users():
    with get_db_connection() as conn:
        with get_cursor(conn) as cur:
            cur.execute("SELECT * FROM users")
            return cur.fetchall()
