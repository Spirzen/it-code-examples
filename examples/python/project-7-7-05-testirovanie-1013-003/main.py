from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def run_e2e_scenario():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Шаг 1: Регистрация
        driver.get("file:///C:/path/to/index.html")
        
        name_field = driver.find_element(By.ID, "name")
        email_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        name_field.send_keys("TestUser")
        email_field.send_keys("testuser@example.com")
        password_field.send_keys("securepass")
        
        submit_button.click()
        
        # Ожидание сообщения об успехе
        success_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "successMessage"))
        )
        assert "Успешная регистрация" in success_msg.text
        
        # Шаг 2: после "успеха" форма должна очиститься (или скрыться)
        # ❌ Анти-паттерн: time.sleep(2) — флейк на медленной машине.
        # ✅ Явное ожидание: поле пустое или исчезло сообщение об успехе.
        WebDriverWait(driver, 10).until(
            lambda d: name_field.get_attribute("value") == ""
        )
        
        # Проверка очистки формы
        assert name_field.get_attribute("value") == ""
        assert email_field.get_attribute("value") == ""
        assert password_field.get_attribute("value") == ""
        
        print("Сценарий E2E завершен: регистрация прошла успешно, данные очищены.")
        
        # Добавление товара в корзину (симуляция)
        # Представим, что мы уже на странице магазина
        driver.get("file:///C:/path/to/cart.html") # Допустим, такой файл существует
        
        add_to_cart_btn = driver.find_element(By.CLASS_NAME, "add-to-cart-btn")
        add_to_cart_btn.click()
        
        confirmation = driver.find_element(By.CLASS_NAME, "cart-confirm")
        assert "Товар добавлен" in confirmation.text
        
        print("Товар добавлен в корзину успешно.")
        
    except Exception as e:
        print(f"Ошибка E2E сценария: {e}")
        # Сохранение скриншота для анализа
        driver.save_screenshot("e2e_error.png")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_e2e_scenario()
