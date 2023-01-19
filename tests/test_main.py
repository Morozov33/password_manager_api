from fastapi.testclient import TestClient
# from sqlmodel import Session
from passlib.hash import cisco_type7 as ct7
# from password_manager.main import Passwords


def test_create_password(client: TestClient):
    response = client.post(
                "/password/yandex",
                json={"password": "secret_word"},
    )
    data = response.json()

    assert response.status_code == 200
    assert ct7.verify("secret_word", data["password"])
    assert data["service_name"] == "yandex"
