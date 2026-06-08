from pymongo import MongoClient

import psycopg2

pg = psycopg2.connect("...")
mongo = MongoClient("...")

with pg.cursor() as cur:
    cur.execute("SELECT id, name, email FROM users")
    for row in cur:
        user = {
            "_id": row[0],
            "name": row[1],
            "email": row[2],
            "orders": []  # будет заполнено далее
        }
        mongo.universe.users.insert_one(user)

    # Затем orders + join в памяти или bulk_write
