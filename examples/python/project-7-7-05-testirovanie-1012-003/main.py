
import requests

BASE_URL = "http://localhost:8000"

def test_create_and_read_user():
    payload = {"name": "Test User", "email": "test.user@example.com"}

    create_resp = requests.post(f"{BASE_URL}/users/", json=payload, timeout=5)
    assert create_resp.status_code == 201
    created = create_resp.json()
    assert created["email"] == payload["email"]

    user_id = created["id"]
    read_resp = requests.get(f"{BASE_URL}/users/{user_id}", timeout=5)
    assert read_resp.status_code == 200
    loaded = read_resp.json()
    assert loaded["name"] == payload["name"]
