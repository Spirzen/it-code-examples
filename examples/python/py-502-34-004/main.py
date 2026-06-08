users = {}  # временное хранилище

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Поле name обязательно'}), 400

    user_id = max(users.keys(), default=0) + 1
    user = {'id': user_id, 'name': data['name'], 'email': data.get('email')}
    users[user_id] = user
    return jsonify(user), 201

@app.route('/api/users/<int:user_id>', methods=['GET'])
def read_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'Пользователь не найден'}), 404
    return jsonify(user)

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'Пользователь не найден'}), 404
    data = request.get_json()
    users[user_id].update({
        'name': data.get('name', users[user_id]['name']),
        'email': data.get('email', users[user_id]['email'])
    })
    return jsonify(users[user_id])

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'Пользователь не найден'}), 404
    del users[user_id]
    return '', 204
