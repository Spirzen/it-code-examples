
import urllib.request

def make_request(url):
    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')
        print(f"Статус: {response.status}")
        print(f"Ответ сервера:\n{Данные}")
    except Exception as e:
        print(f"Ошибка при подключении: {e}")

if __name__ == "__main__":
    url = "http://localhost:8000"
    make_request(url)
