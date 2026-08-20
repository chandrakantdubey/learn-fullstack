from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/tasks"

    model_config = SettingsConfigDict(env_prefix="APP_", case_sensitive=False)


settings = Settings()
