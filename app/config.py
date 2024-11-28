from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Xenara FastAPI"
    database_url: str = "sqlite:///./test.db"
    mongo_uri: str  # Reads XENARA_MONGO_URI from the .env file
    pinecone_secret: str  # Reads PINECONE_DB_SECRET from the .env file

    class Config:
        env_file = "../.env"

# Create an instance of Settings
settings = Settings()
