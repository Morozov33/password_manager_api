## Test task on FastAPI.
### Status: [![linter](https://github.com/Morozov33/password_manager_api/actions/workflows/linter.yml/badge.svg)](https://github.com/Morozov33/password_manager_api/actions/workflows/linter.yml)  [![tests](https://github.com/Morozov33/password_manager_api/actions/workflows/tests.yml/badge.svg)](https://github.com/Morozov33/password_manager_api/actions/workflows/tests.yml)  [![Maintainability](https://api.codeclimate.com/v1/badges/8c12d1c0635c6ae739c6/maintainability)](https://codeclimate.com/github/Morozov33/password_manager_api/maintainability)  [![Test Coverage](https://api.codeclimate.com/v1/badges/8c12d1c0635c6ae739c6/test_coverage)](https://codeclimate.com/github/Morozov33/password_manager_api/test_coverage)
### It's usinig: ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)  ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
----
Для запуска на локальной машине:
1. `git clone git@github.com:Morozov33/password_manager_api.git`
2. `cd password_manager_api`
3. `make build` собирает образы и запускает контейнеры приложения в фоновом режиме. При сборке используются образы `python:3.10-slim` и `postgres:13.9-alpine`
4. При сборке запускаются тесты. Посмотреть результаты тестов: `make result`
5. Приложение доступно по адресу: `127.0.0.1:8000`
6. Остановка контейнеров `make stop`
7. Запуск контейнеров `make start`
----
Простой менеджер паролей. Пароли хранятся в БД Postgres, зашифрованные с помошью алгоритма Cisco “Type 7” (не является полноценным хешем, т.к. возможно обратное декодирование, используется в демонстрационных целях).  
Доступны все CRUD операции:
1. Создание или обновление пары "пароль-сервис":
    ```POST /password/google
        content-type: application/json

        {
            "password": "secret_word_for_google"
        }

        HTTP/1.1 200 OK
    ```
    P.S. Так же можно было бы разделить операции создания и обновления на два метода `POST` и `PATCH`, используя два роута, и изолировать эти функции друг от друга.
2. Запрос пароля по имени сервиса:
    ```GET /password/google

        HTTP/1.1 200 OK
        content-type: application/json
        {
            "password": "secret_word_for_google",
            "service_name": "google"
        }
    ```
3. Удаление пары "пароль-сервис" (добавлено опционально, для полноты CRUD-операций):
    ```DELETE /password/google

        HTTP/1.1 200 OK
        content-type: application/json
        {
            "ok": True
        }
    ```
4. Поиск по части имени сервиса. Поиск регистронезависимый, результат - список. Запрос с параметром `?service_name=` приведет к ошибке `400`:
    ```GET /password/?service_name=go

        HTTP/1.1 200 OK
        content-type: application/json
        [
            {
                "password": "secret_word_for_google",
                "service_name": "google"
            },
            {
                "password": "secret_word_for_mongo_db",
                "service_name": "mongo_db"
            }
        ]
    ```
