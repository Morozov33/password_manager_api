import os
from pathlib import Path
from dotenv import load_dotenv
from sqlmodel import SQLModel, Session, create_engine


def get_database_url():

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Load envroinments variable
    env_path = os.path.join(BASE_DIR, '.env')
    load_dotenv(dotenv_path=env_path)

    # Get database url
    database_url = os.getenv("DATABASE_URL")
    return database_url


# Create engine for DB
engine = create_engine(get_database_url(), echo=True)


def create_tables():
    SQLModel.metadata.create_all(engine)


def get_session():

    # Return generator for database connection
    with Session(engine) as session:
        yield session
