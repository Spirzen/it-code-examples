from urllib.parse import urlparse

import urllib.request

def analyze_and_check(url):
    parsed = urlparse(url)
    
    print(f"URL: {url}")
    print(f"Схема: {parsed.scheme}")
    print(f"Домен: {parsed.netloc}")
    print(f"Путь: {parsed.path}")
    print(f"Параметры: {parsed.query}")
    
    try:
        response = urllib.request.urlopen(url, timeout=5)
        print(f"Статус доступности: OK ({response.status})")
    except urllib.error.URLError as e:
        print(f"Ошибка доступа: {e.reason}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

if __name__ == "__main__":
    test_url = "https://www.example.com"
    analyze_and_check(test_url)
