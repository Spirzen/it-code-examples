# Инициализация для Адама
weights = np.zeros(n_features)
bias = 0.0
m_w = np.zeros(n_features)  # Первый момент весов
v_w = np.zeros(n_features)  # Второй момент весов
m_b = 0.0
v_b = 0.0
beta1 = 0.9
beta2 = 0.999
epsilon = 1e-8
t = 0

for epoch in range(n_epochs):
    indices = np.random.permutation(len(X_train_scaled))
    for i in range(0, len(X_train_scaled), batch_size):
        t += 1
        batch_indices = indices[i:i + batch_size]
        X_batch = X_train_scaled[batch_indices]
        y_batch = y_train_scaled[batch_indices]
        
        predictions = X_batch @ weights + bias
        errors = predictions - y_batch
        
        grad_weights = (X_batch.T @ errors) / len(batch_indices)
        grad_bias = errors.mean()
        
        # Обновление первого момента
        m_w = beta1 * m_w + (1 - beta1) * grad_weights
        m_b = beta1 * m_b + (1 - beta1) * grad_bias
        
        # Обновление второго момента
        v_w = beta2 * v_w + (1 - beta2) * (grad_weights ** 2)
        v_b = beta2 * v_b + (1 - beta2) * (grad_bias ** 2)
        
        # Коррекция смещения
        m_w_hat = m_w / (1 - beta1 ** t)
        v_w_hat = v_w / (1 - beta2 ** t)
        m_b_hat = m_b / (1 - beta1 ** t)
        v_b_hat = v_b / (1 - beta2 ** t)
        
        # Обновление параметров
        weights -= learning_rate * m_w_hat / (np.sqrt(v_w_hat) + epsilon)
        bias -= learning_rate * m_b_hat / (np.sqrt(v_b_hat) + epsilon)
