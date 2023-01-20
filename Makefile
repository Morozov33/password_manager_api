build: # Building Docker images and start: test, app and db
	docker compose -f docker-compose.yml -f docker-compose.tests.yml up -d --build

start: # Start Docker containers: app and db
	docker compose start password_app

stop: # Stop Docker containers
	docker compose stop password_app db_postgres

result: # Show tests result
	docker logs tests_password_app

localstart: # Use last migration and local start uvicorn server for app
	export DATABASE_URL=postgresql+psycopg2://postgres@localhost/passwords_db && poetry run alembic upgrade head && poetry run uvicorn password_manager.main:app --reload

lint: #linter for code
	poetry run flake8 password_manager tests

migrate: #make local migrations by Alembic
	export DATABASE_URL=postgresql+psycopg2://postgres@localhost/<database_name> &&
	poetry run alembic revision --autogenerate -m "New migrate"

test: #local start pytest
	export DATABASE_URL=sqlite:// && poetry run pytest

coverage: #start code coverage and write report is xml-file for CodeClimate
	poetry run pytest --cov-report xml --cov=password_manager tests/
