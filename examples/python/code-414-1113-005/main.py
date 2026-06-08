
import requests

from requests.exceptions import RequestException

def fetch_user_data(user_id: int, timeout: float = 5.0) -> dict:
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError("user_id must be a positive integer")

    url = f"https://api.example.com/users/{user_id}"
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except RequestException as exc:
        raise RuntimeError(f"Failed to fetch user {user_id}") from exc
