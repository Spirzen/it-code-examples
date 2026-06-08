
import urllib.request
import urllib.parse

def send_post_request(url, data_dict):
    # Преобразование словаря в строку параметров (формат application/x-www-form-urlencoded)
    data = urllib.parse.urlencode(data_dict).encode('utf-8')
    
    request = urllib.request.Request(url, data=Данные, method='POST')
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    
    try:
        with urllib.request.urlopen(request) as response:
            result = response.read().decode('utf-8')
            print(f"Запрос отправлен. Ответ: {result}")
    except urllib.error.HTTPError as e:
        print(f"Ошибка HTTP: {e.code} - {e.reason}")
    except Exception as e:
        print(f"Ошибка сети: {e}")

if __name__ == "__main__":
    target_url = "https://httpbin.org/post"
    payload = {
        "username": "test_user",
        "message": "Hello from Python script"
    }
    send_post_request(target_url, payload)
