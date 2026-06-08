# Получить всё localStorage как JSON-строка
local_data = driver.execute_script("return JSON.stringify(localStorage);")
data = json.loads(local_data) if local_data else {}

# Получить одно значение
theme = driver.execute_script("return localStorage.getItem('theme');")

# Установить
driver.execute_script("localStorage.setItem('theme', 'dark');")

# Удалить
driver.execute_script("localStorage.removeItem('debug');")

# Очистить
driver.execute_script("localStorage.clear();")
