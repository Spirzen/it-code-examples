# tests/test_users_api.py

import httpx

BASE_URL = "https://jsonplaceholder.typicode.com"  # учебный публичный API

def test_get_user_returns_200_and_name():
    # Act — вызываем API (аналог вкладки Postman / curl)
    response = httpx.get(f"{BASE_URL}/users/1", timeout=10.0)

    # Assert — оракул: статус и структура ответа
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert "name" in body
