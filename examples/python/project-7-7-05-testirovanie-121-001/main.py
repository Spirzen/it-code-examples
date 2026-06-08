
import httpx

def test_create_post_integration():
    # Arrange — тестовое тело (в проекте часто из фикстуры или factory)
    payload = {"title": "QA order", "body": "integration check", "userId": 1}

    # Act
    response = httpx.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload,
        timeout=10.0,
    )

    # Assert — контракт: создание → 201 и эхо полей
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert "id" in data  # сервер вернул идентификатор созданной сущности
