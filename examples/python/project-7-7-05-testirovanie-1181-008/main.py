
import json

with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    driver.get("https://example.com/login")
    # ... выполнить логин

    # Дождаться успешного входа
    wait.until(EC.url_contains("/dashboard"))

    # Сохранить cookies
    cookies = driver.get_cookies()
    with open("session.json", "w", encoding="utf-8") as f:
        json.dump(cookies, f, indent=2)
    print("✅ Сессия сохранена в session.json")
