start: # Use last migration and local start uvicorn server for app
	# for local start it needs DATABASE_URL, for example, uncomment next line:
	# export DATABASE_URL=postgresql+psycopg2://postgres@localhost/<database_name>
	poetry run alembic upgrade head
	poetry run uvicorn password_manager.main:app --reload

lint: #linter for code
	poetry run flake8 password_manager tests

migrate: #make local migrations by Alembic
	# for local start it needs DATABASE_URL, for example, uncomment next line:
	# export DATABASE_URL=postgresql+psycopg2://postgres@localhost/<database_name>
	poetry run alembic revision --autogenerate -m "New migrate"

test: #local start pytest
	export DATABASE_URL=sqlite:// && poetry run pytest

coverage: #start code coverage and write report is xml-file for CodeClimate
	poetry run pytest --cov-report xml --cov=password_manager tests/
