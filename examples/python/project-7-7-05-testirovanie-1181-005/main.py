from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import time

with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    driver.get("https://news.yandex.ru")
    
    wait = WebDriverWait(driver, 10)
    
    # Дождаться первой новости
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "news-item")))

    # Прокрутка до конца (3 раза)
    for _ in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)  # имитация загрузки

    # Сбор всех заголовков
    titles = driver.find_elements(By.CSS_SELECTOR, ".news-item__title")
    print(f"Найдено {len(titles)} заголовков:")
    
    for i, title in enumerate(titles[:10], 1):  # первые 10
        print(f"{i}. {title.text}")

    # Сохранить в файл
    with open("headlines.txt", "w", encoding="utf-8") as f:
        for title in titles:
            f.write(title.text + "\n")
    print("✅ Заголовки сохранены в headlines.txt")
