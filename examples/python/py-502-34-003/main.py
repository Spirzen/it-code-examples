from flask import session

app.secret_key = 'очень-секретный-ключ-никому-не-говорите'  # обязательно!

@app.route('/login', methods=['POST'])
def login():
    session['user_id'] = 123
    return 'Вы вошли'

@app.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return 'Неавторизован', 401
    return f'Профиль пользователя {user_id}'
