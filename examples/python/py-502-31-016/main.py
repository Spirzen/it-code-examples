headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
}

params = {'q': 'laptop', 'page': 1}

try:
    response = requests.get(
        'https://example-shop.com/search',
        params=params,
        headers=headers,
        timeout=10  # Секунды
    )
    response.raise_for_status()  # Выбрасывает исключение при 4xx/5xx
except requests.RequestException as e:
    print(f"Ошибка запроса: {e}")
