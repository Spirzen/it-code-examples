agree = driver.find_element(By.ID, "agree")
basic_plan = driver.find_element(By.CSS_SELECTOR, "input[value='basic']")
premium_plan = driver.find_element(By.CSS_SELECTOR, "input[value='premium']")

# Проверить текущее состояние
print("Согласен:", agree.is_selected())      # → False (если не checked)
print("Тариф 'basic' выбран:", basic_plan.is_selected())  # → True

# Переключить чекбокс
if not agree.is_selected():
    agree.click()  # теперь is_selected() == True

# Выбрать другой тариф
if not premium_plan.is_selected():
    premium_plan.click()  # автоматически снимет 'basic'
