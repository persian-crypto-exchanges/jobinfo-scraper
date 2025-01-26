import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV: str = os.getenv("ENV", "development")
    # Add other settings here, e.g.:
    # DATABASE_URL: str = ...

    class Config:
        env_file = ".env"


settings = Settings()
