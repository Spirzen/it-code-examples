# 1. Запоминаем дескриптор текущей вкладки
main_handle = driver.current_window_handle

# 2. Открываем новую вкладку
driver.execute_script("window.open('https://example.com');")

# 3. Получаем список всех вкладок
handles = driver.window_handles  # например: ['CDwindow-1', 'CDwindow-2']

# 4. Переключаемся на новую (последнюю)
new_handle = handles[-1]
driver.switch_to.window(new_handle)

# 5. Работаем с новой вкладкой
print("Текущий URL:", driver.current_url)

# 6. Возвращаемся на основную
driver.switch_to.window(main_handle)
