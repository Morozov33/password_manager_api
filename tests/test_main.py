from fastapi.testclient import TestClient
from sqlmodel import Session
from password_manager.main import Passwords


def test_create_password(client: TestClient):
    response = client.post(
                "/password/yandex",
                json={"password": "secret_word"},
    )
    data = response.json()

    assert response.status_code == 200
    assert data["password"] == "secret_word"
    assert data["service_name"] == "yandex"
