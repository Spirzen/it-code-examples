@pytest.fixture
def auth_headers(client):
    r = client.post(
        "/token",
        data={"username": "demo", "password": "demo123"},
    )
    token = r.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_notes_require_auth(client):
    assert client.get("/notes").status_code == 401


def test_notes_with_token(client, auth_headers):
    assert client.get("/notes", headers=auth_headers).status_code == 200
