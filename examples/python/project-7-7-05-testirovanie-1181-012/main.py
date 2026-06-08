
import json
import time

from datetime import datetime

def load_session():
    with open("bank_session.json") as f:
        return json.load(f)

def save_session(driver):
    cookies = driver.get_cookies()
    # Удаляем expiry для будущих запусков
    for c in cookies:
        c.pop("expiry", None)
    with open("bank_session.json", "w") as f:
        json.dump(cookies, f)

def check_balance():
    options = Options()
    options.add_argument("--headless=new")  # без GUI
    with webdriver.Chrome(service=Service(...), options=options) as driver:
        driver.get("https://bank.example.com")

        # Восстановить сессию
        for cookie in load_session():
            driver.add_cookie(cookie)
        driver.refresh()

        # Дождаться загрузки
        wait = WebDriverWait(driver, 20)
        balance_el = wait.until(EC.visibility_of_element_located((By.ID, "balance")))
        balance = balance_el.text.replace("₽", "").replace(" ", "")

        print(f"[{datetime.now()}] Баланс: {balance} ₽")
        return float(balance)

# Первичная настройка (вручную!)
# 1. Запустить браузер без headless
# 2. Войти вручную
# 3. Вызвать save_session(driver)

# Регулярная проверка
while True:
    try:
        check_balance()
    except Exception as e:
        print("❌ Ошибка:", e)
    time.sleep(3600)  # 1 час
