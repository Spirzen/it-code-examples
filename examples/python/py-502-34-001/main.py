from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # ... проверка учётных данных
        return f'Вход выполнен: {username}'
    else:
        return '''
            <form method="post">
                <input name="username" placeholder="Имя"><br>
                <input name="password" type="password" placeholder="Пароль"><br>
                <button type="submit">Войти</button>
            </form>
        '''
