# views.py — слой представления

import sqlite3

def get_order_view(order_id):
    # Прямой доступ к БД из view нарушает слоистую архитектуру
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
    row = cursor.fetchone()

    # Смешение бизнес-логики и представления
    if row[3] > 1000:
        discount = row[3] * 0.1
    else:
        discount = 0

    return {
        "id": row[0],
        "total": row[3] - discount,
        "status": row[4]
    }
