# Добавить cookie (должна соответствовать текущему domain/path)
driver.add_cookie({
    "name": "lang",
    "value": "en",
    "domain": ".example.com",
    "path": "/",
    "secure": False
})

# Удалить одну
driver.delete_cookie("lang")

# Удалить все
driver.delete_all_cookies()
