# tests/test_api.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_create_note():
    r = client.post("/notes", json={"text": "pytest"})
    assert r.status_code == 201
    body = r.json()
    assert body["text"] == "pytest"
    assert "id" in body


def test_create_note_validation():
    r = client.post("/notes", json={"text": ""})
    assert r.status_code == 422
