## Test task for DidenokTeam company.
### Status: [![linter](https://github.com/Morozov33/password_manager_api/actions/workflows/linter.yml/badge.svg)](https://github.com/Morozov33/password_manager_api/actions/workflows/linter.yml)
### It's usinig: ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
----
Для запуска на локальном сервере:
1. В файл `.env.example` добавить переменную `POSTGRES_DB_URL`.
2. Изменить имя файла `.env.example` на `.env`.
3. Запуск локального сервера с приложением командой `make start` из директории проекта. Устанавливаются все зависимости и к БД, указанной в переменной в `POSTGRES_DB_URL`, применяется последняя миграция из папки `foods_menu_api/migrations/versions`. После остановки приложения из базы данных удаляются все записи.
----
