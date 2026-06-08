last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Прокрутить в самый низ
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Ждать подгрузки (5 сек или появления индикатора)
    time.sleep(2)
    
    # Проверить, изменилась ли высота
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break  # дальше некуда
    last_height = new_height

# Теперь собираем данные
items = driver.find_elements(By.CLASS_NAME, "product")
print(f"Загружено {len(items)} товаров.")
