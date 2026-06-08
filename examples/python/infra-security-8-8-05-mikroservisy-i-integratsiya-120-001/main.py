
import requests
import time

def poll_for_updates(endpoint: str, timeout: int = 30):
    while True:
        try:
            response = requests.get(
                endpoint,
                params={"timeout": timeout},  # сервер удерживает соединение до появления данных
                timeout=timeout + 5
            )
            if response.status_code == 200 and response.content:
                yield response.json()
            # При 204 No Content или пустом теле — немедленный повтор
        except requests.exceptions.Timeout:
            continue
        except Exception as e:
            time.sleep(5)  # экспоненциальная задержка при ошибках
