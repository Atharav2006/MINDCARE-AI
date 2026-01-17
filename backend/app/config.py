from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # -----------------------------
    # Core App Settings
    # -----------------------------
    APP_NAME: str = "MindCare-AI Backend"
    ENVIRONMENT: str = Field("development", env="ENVIRONMENT")
    DEBUG: bool = Field(False, env="DEBUG")

    # -----------------------------
    # Server
    # -----------------------------
    HOST: str = Field("0.0.0.0", env="HOST")
    PORT: int = Field(8000, env="PORT")

    # -----------------------------
    # Security
    # -----------------------------
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(60 * 24, env="ACCESS_TOKEN_EXPIRE_MINUTES")

    # -----------------------------
    # CORS
    # -----------------------------
    ALLOWED_ORIGINS: List[str] = Field(
        default_factory=lambda: ["http://localhost:3000"]
    )

    # -----------------------------
    # AI / External Services
    # -----------------------------
    EMOTION_SERVICE_URL: str = Field(
        "http://localhost:9000", env="EMOTION_SERVICE_URL"
    )

    # -----------------------------
    # Logging
    # -----------------------------
    LOG_LEVEL: str = Field("INFO", env="LOG_LEVEL")

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

