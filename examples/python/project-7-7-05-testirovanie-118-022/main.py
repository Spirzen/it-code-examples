
import pytest
import psycopg2

@pytest.fixture(scope="function")
def db_connection():
    conn = psycopg2.connect("dbname=test user=postgres password=secret")
    yield conn
    conn.close()

@pytest.fixture(scope="function")
def transaction(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("BEGIN")
    yield cursor
    cursor.execute("ROLLBACK")
    cursor.close()
