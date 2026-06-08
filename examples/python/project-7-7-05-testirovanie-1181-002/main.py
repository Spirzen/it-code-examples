from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    driver.get("https://example.com/register")

    wait = WebDriverWait(driver, 10)

    # 1. Ждём, пока форма прогрузится
    form = wait.until(EC.presence_of_element_located((By.ID, "registration-form")))

    # 2. Находим поля
    email = driver.find_element(By.ID, "email")
    password = driver.find_element(By.NAME, "password")
    country = Select(driver.find_element(By.ID, "country"))
    terms = driver.find_element(By.ID, "agree-terms")
    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # 3. Заполняем
    email.clear()
    email.send_keys("test@example.com")

    password.clear()
    password.send_keys("SecurePass123!")

    # 4. Выбираем страну
    country.select_by_visible_text("Россия")

    # 5. Ставим галочку (если не стоит)
    if not terms.is_selected():
        terms.click()

    # 6. Отправляем — с ожиданием кликабельности
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit.click()

    # 7. Проверяем результат
    success = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-success")))
    assert "Регистрация успешна" in success.text
    print("✅ Регистрация прошла успешно.")
