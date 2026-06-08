from flask import Flask, request, jsonify

import time
import random

app = Flask(__name__)

@app.route('/order', methods=['POST'])
def process_order():
    # Имитация задержки обработки заказа (от 0.1 до 0.5 секунд)
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)
    
    # Возвращаем успешный ответ
    return jsonify({
        "status": "success",
        "message": "Заказ оформлен успешно",
        "order_id": random.randint(10000, 99999),
        "processing_time_ms": int(delay * 1000)
    }), 200

if __name__ == '__main__':
    # Запуск сервера на локальном хосте, порт 5000
    app.run(host='127.0.0.1', port=5000, debug=False)
