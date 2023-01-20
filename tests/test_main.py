from fastapi.testclient import TestClient
from sqlmodel import Session
from password_manager.hash import get_hash
from password_manager.main import Passwords


def test_create_password(client: TestClient):
    response = client.post(
                "/password/yandex",
                json={"password": "secret word"},
    )
    data = response.json()

    assert response.status_code == 200
    assert data["password"] == "secret word"
    assert data["service_name"] == "yandex"


def test_create_password_incomplete(client: TestClient):

    # title has an invalid type: None, int, ets.
    response = client.post(
                "/password/yandex",
                json={"not_password": "secret word"},
    )
    assert response.status_code == 422

    response = client.post(
                "/password/yandex",
                json={"password": {"secret": "word"}},
    )
    assert response.status_code == 422

    response = client.post(
                "/password/yandex",
                json={"password": None},
    )
    assert response.status_code == 422


def test_read_empty_password(session: Session, client: TestClient):
    response = client.get("/password/google")

    assert response.status_code == 404


def test_read_password(session: Session, client: TestClient):
    password_1 = Passwords(
            password=get_hash("secret_word"),
            service_name="google"
    )
    session.add(password_1)
    session.commit()

    response = client.get("/password/google")
    data = response.json()

    assert response.status_code == 200
    assert data["password"] == "secret_word"
    assert data["service_name"] == password_1.service_name


def test_update_password(session: Session, client: TestClient):
    password_1 = Passwords(
            password=get_hash("secret_word"),
            service_name="google"
    )
    session.add(password_1)
    session.commit()

    response = client.post(
                "/password/google",
                json={"password": "update secret_word"},
    )
    data = response.json()

    assert response.status_code == 200
    assert not data["password"] == "secret_word"
    assert data["password"] == "update secret_word"
    assert data["service_name"] == "google"


def test_delete_password(session: Session, client: TestClient):
    password_1 = Passwords(
            password=get_hash("secret word"),
            service_name="google"
    )
    session.add(password_1)
    session.commit()

    response = client.delete("/password/google")
    db_password = session.get(Passwords, password_1.id)

    assert response.status_code == 200
    assert db_password is None


def test_get_passwords_for_part_of_service_name(
                                        session: Session,
                                        client: TestClient
):
    service_names_list = [
            "xxx",
            "xxmail",
            "mailxx",
            "abxxcd",
            "xabcx",
            "google",
            "yandex",
            "mail"
    ]

    for name in service_names_list:
        session.add(
            Passwords(
                password=get_hash(f"secret_word_for_{name}"),
                service_name=name
            )
        )

    session.commit()

    response = client.get("/password/?service_name=xx")
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 4
    for item in data:
        assert "xx" in item["service_name"]


def test_get_passwords_for_empty_part_of_service_name(
                                        session: Session,
                                        client: TestClient
):

    response = client.get("/password/?service_name=")

    assert response.status_code == 400
