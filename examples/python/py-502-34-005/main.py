
import requests
import logging
import time

from typing import List, Dict, Any

logger = logging.getLogger(__name__)

def fetch_github_repos(username: str, token: str = None) -> List[Dict[str, Any]]:
    """
    Получает все публичные репозитории пользователя GitHub.
    Поддерживает пагинацию (до 1000 репозиториев — лимит GitHub).
    Возвращает список словарей с ключами: name, description, html_url, stargazers_count.
    """
    base_url = f'https://api.github.com/users/{username}/repos'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    if token:
        headers['Authorization'] = f'Bearer {token}'

    session = requests.Session()
    session.headers.update(headers)

    repos = []
    page = 1
    per_page = 100  # максимум, разрешённый GitHub

    while True:
        try:
            response = session.get(
                base_url,
                params={'page': page, 'per_page': per_page},
                timeout=(5, 30)
            )

            # Явная обработка статусов
            if response.status_code == 403:
                # Превышен лимит запросов (Rate Limit)
                reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
                sleep_duration = max(reset_time - time.time(), 60)
                logger.warning(f"Rate limit exceeded. Пауза на {sleep_duration:.0f} сек.")
                time.sleep(sleep_duration)
                continue  # повторить тот же запрос
            elif response.status_code == 404:
                raise ValueError(f"Пользователь '{username}' не найден на GitHub.")
            elif response.status_code != 200:
                response.raise_for_status()  # выбросит исключение для 5xx и других 4xx

            page_data = response.json()
            if not page_data:  # пустой ответ — конец пагинации
                break

            # Извлекаем только нужные поля
            for repo in page_data:
                repos.append({
                    'name': repo['name'],
                    'description': repo.get('description'),
                    'html_url': repo['html_url'],
                    'stargazers_count': repo.get('stargazers_count', 0)
                })

            # Проверяем, есть ли следующая страница (заголовок Link)
            link_header = response.headers.get('Link')
            if not link_header or 'rel="next"' not in link_header:
                break
            page += 1

        except requests.RequestException as e:
            logger.error(f"Ошибка при запросе к GitHub (страница {page}): {e}")
            raise

    return repos
