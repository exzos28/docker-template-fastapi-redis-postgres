from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    fast_api_port: int = Field(..., env='FAST_API_PORT')
    port: int = Field(..., env='PORT')
    host: str = Field(..., env='HOST')
    postgres_user: str = Field(..., env='POSTGRES_USER')
    postgres_password: str = Field(..., env='POSTGRES_PASSWORD')
    postgres_db: str = Field(..., env='POSTGRES_DB')
    postgres_port: int = Field(..., env='POSTGRES_PORT')

    @property
    def postgresql_uri(self):
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@db:{self.postgres_port}/{self.postgres_db}"


settings = Settings()
