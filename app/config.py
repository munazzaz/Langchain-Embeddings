from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Xenara FastAPI"
    database_url: str = "sqlite:///./test.db"
    mongo_uri: str  # Reads XENARA_MONGO_URI from the .env file
    pinecone_secret: str  # Reads PINECONE_DB_SECRET from the .env file
    hugging_face_model: str = "sentence-transformers/all-MiniLM-L6-v2"  # Default HuggingFace model
    
    class Config:
        env_file = "app/.env"

# Create an instance of Settings
settings = Settings()
