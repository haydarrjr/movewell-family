"""Application settings using Pydantic BaseSettings (Environment driven, zero secrets)."""
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Movewell Family Engine"
    environment: str = os.getenv("MOVEWELL_ENV", "development")
    host: str = os.getenv("MOVEWELL_HOST", "0.0.0.0")
    port: int = int(os.getenv("MOVEWELL_PORT", "8000"))
    secret_key: str = os.getenv("MOVEWELL_SECRET_KEY", "default-dev-secret-change-in-prod")
    
    # Integrations (Read strictly from environment)
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o")
    hevy_api_key: str | None = os.getenv("HEVY_API_KEY")

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
