from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    wait = WebDriverWait(driver, 15)

    # 1. Открыть и дождаться загрузки SPA
    driver.get("https://app.example.com/login")
    wait.until(EC.title_contains("Вход"))  # SPA мог переопределить title позже

    # 2. Дождаться формы (может инициализироваться асинхронно)
    form = wait.until(EC.presence_of_element_located((By.ID, "login-form")))

    # 3. Заполнить поля
    email = wait.until(EC.element_to_be_clickable((By.ID, "email")))
    password = driver.find_element(By.ID, "password")  # уже есть, если форма загружена

    email.clear()
    email.send_keys("user@test.com")
    password.send_keys("pass123")

    # 4. Отправить — и дождаться редиректа
    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

    # Ждём, пока URL изменится на /dashboard
    wait.until(EC.url_contains("/dashboard"))

    # 5. Проверяем, что пользователь вошёл
    user_menu = wait.until(EC.visibility_of_element_located((By.ID, "user-menu")))
    assert "user@test.com" in user_menu.text

    print("✅ Авторизация успешна.")
