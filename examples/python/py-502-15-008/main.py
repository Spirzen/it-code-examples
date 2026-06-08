# Замалчивание ошибки — плохая практика
try:
    value = int(user_input)
except ValueError:
    pass  # Ошибка проигнорирована

# Явная обработка с логированием
try:
    value = int(user_input)
except ValueError as error:
    log_error(f"Неверный формат числа: {user_input}")
    raise  # Передача ошибки выше для принятия решения

# Явное игнорирование только при осознанном выборе
try:
    cleanup_temp_files()
except FileNotFoundError:
    # Ожидаемое отсутствие временных файлов — безопасно игнорировать
    pass
