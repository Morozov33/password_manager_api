## Test task on FastAPI.
### Status: [![linter](https://github.com/Morozov33/password_manager_api/actions/workflows/linter.yml/badge.svg)](https://github.com/Morozov33/password_manager_api/actions/workflows/linter.yml)  [![tests](https://github.com/Morozov33/password_manager_api/actions/workflows/tests.yml/badge.svg)](https://github.com/Morozov33/password_manager_api/actions/workflows/tests.yml)  [![Maintainability](https://api.codeclimate.com/v1/badges/8c12d1c0635c6ae739c6/maintainability)](https://codeclimate.com/github/Morozov33/password_manager_api/maintainability)  [![Test Coverage](https://api.codeclimate.com/v1/badges/8c12d1c0635c6ae739c6/test_coverage)](https://codeclimate.com/github/Morozov33/password_manager_api/test_coverage)
### It's usinig: ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)  ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
----
Для запуска на локальном сервере:

1. В файл `docker compose -f docker-compose.yml -f docker-compose.tests.yml up -d --build` добавить переменную `DATABASE_URL`.
2. Изменить имя файла `docker compose up -d` на `.env`.
3. Запуск локального сервера с приложением командой `docker compose down --remove-orphans` из директории проекта. Устанавливаются все зависимости и к БД, указанной в переменной в `DATABASE_URL`, применяется последняя миграция из папки `foods_menu_api/migrations/versions`. После остановки приложения из базы данных удаляются все записи.
----
