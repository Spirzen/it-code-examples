from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Фоновый режим
driver = webdriver.Chrome(options=options)

try:
    driver.get('https://dynamic-shop.com/products')

    # Ожидание появления элементов
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'product-item')))

    # Прокрутка до конца (если есть lazy loading)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Парсинг через BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    prices = [p.get_text() for p in soup.find_all('span', class_='price')]

finally:
    driver.quit()
