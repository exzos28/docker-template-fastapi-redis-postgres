import os

from pydantic import BaseSettings

from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    fast_api_port: int = os.getenv('FAST_API_PORT')
    port: int = os.getenv('PORT')
    host: str = os.getenv('HOST')
    postgres_user: str = os.getenv('POSTGRES_USER')
    postgres_password: str = os.getenv('POSTGRES_PASSWORD')
    postgres_db: str = os.getenv('POSTGRES_DB')
    postgres_port: int = os.getenv('POSTGRES_PORT')

    @property
    def postgresql_uri(self):
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@localhost/{self.postgres_db}"


settings = Settings()
