from flask import Flask, request

import sqlite3

app = Flask(__name__)

@app.route('/search')
def search():
    query = request.args.get('q')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Уязвимость: прямая интерполяция пользовательского ввода
    cursor.execute("SELECT * FROM users WHERE name = '" + query + "'")
    results = cursor.fetchall()
    conn.close()
    return str(results)
