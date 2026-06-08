# После логина — сохраняем
token = driver.execute_script("return localStorage.getItem('authToken');")
if token:
    with open("auth_token.txt", "w") as f:
        f.write(token)

# В новом сценарии — восстанавливаем
with open("auth_token.txt") as f:
    token = f.read().strip()

driver.get("https://spa-app.com")
driver.execute_script(f"localStorage.setItem('authToken', '{token}');")
driver.refresh()

# Проверяем — пользователь в системе
wait.until(EC.presence_of_element_located((By.ID, "user-panel")))
