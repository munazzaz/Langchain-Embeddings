from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Xenara FastAPI"
    database_url: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

settings = Settings()
