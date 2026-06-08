from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import time

def test_registration_form():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") # Запуск в фоновом режиме
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # Открытие сайта
        driver.get("file:///C:/path/to/index.html") # Укажите путь к вашему файлу
        
        wait = WebDriverWait(driver, 10)
        
        # Поиск элементов
        name_field = driver.find_element(By.ID, "name")
        email_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        # Заполнение невалидными данными
        name_field.clear()
        email_field.clear()
        password_field.clear()
        
        email_field.send_keys("invalid-email")
        password_field.send_keys("123")
        
        submit_button.click()
        
        # Ожидание появления элемента ошибки
        error_email = wait.until(EC.visibility_of_element_located((By.ID, "errorEmail")))
        
        # Проверка текста ошибки
        assert "корректный адрес" in error_email.text.lower(), "Ошибка формата email не отображена"
        
        print("Тест пройден: проверка невалидного email выполнена успешно.")
        
    except Exception as e:
        print(f"Ошибка при выполнении теста: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_registration_form()
