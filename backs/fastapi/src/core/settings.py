from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    debug: bool = False
    sqlalchemy_database_url: str

    class Config:
        env_file = ".env"


@lru_cache()
def settings() -> Settings:
    return Settings()
