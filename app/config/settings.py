from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central application configuration.
    """

    APP_ENV: str = Field(default="development")

    REQUIRE_GEMINI: bool = Field(default=False)

    DATABASE_URL: str

    GEMINI_API_KEY: str = ""

    WHISPER_MODEL: str = "base"

    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"

    SENTIMENT_MODEL: str = (
        "cardiffnlp/twitter-roberta-base-sentiment"
    )

    NER_MODEL: str = "en_core_web_sm"

    CLASSIFICATION_MODEL: str = (
        "facebook/bart-large-mnli"
    )

    FAISS_PATH: str = "data/embeddings"

    LOG_PATH: str = "logs/application.log"

    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()