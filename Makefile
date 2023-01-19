start: #use last migration and start uvicorn server for app
	#poetry run alembic upgrade head
	poetry run uvicorn password_manager.main:app --reload

lint: #linter for code
	poetry run flake8 password_manager tests

migrate: #make migrations by Alembic
	poetry run alembic revision --autogenerate -m "New migrate"

test: #start pytest
	poetry run pytest

coverage: #start code coverage and write report is xml-file for CodeClimate
	poetry run pytest --cov-report xml --cov=password_manager tests/
