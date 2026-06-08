with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    # Сначала открыть домен (иначе add_cookie не сработает)
    driver.get("https://example.com")

    # Загрузить и установить cookies
    with open("session.json", encoding="utf-8") as f:
        cookies = json.load(f)
    for cookie in cookies:
        # Удаляем expiry, если оно прошло (иначе ошибка)
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)

    # Обновить страницу — теперь сервер увидит сессию
    driver.refresh()

    # Проверка
    assert "/dashboard" in driver.current_url
    print("✅ Сессия восстановлена. Вход выполнен без формы.")
