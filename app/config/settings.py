from functools import lru_cache

from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


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

    SENTIMENT_POSITIVE_THRESHOLD: float = 0.05

    SENTIMENT_NEGATIVE_THRESHOLD: float = -0.05

    NER_MODEL: str = "en_core_web_md"

    ENABLE_CUSTOM_ENTITIES: bool = True

    ENABLE_REGEX_ENTITIES: bool = True

    CLASSIFICATION_MODEL: str = (
        "facebook/bart-large-mnli"
    )

    MAX_AUDIO_DURATION_MINUTES: int = 60

    SUPPORTED_AUDIO_FORMATS: str = (
        "wav,mp3,m4a,flac"
    )

    FAISS_PATH: str = "data/embeddings"

    LOG_PATH: str = "logs/application.log"

    LOG_LEVEL: str = "INFO"

    LOG_FORMAT: str = "json"

    @property
    def supported_audio_formats(
        self,
    ) -> list[str]:
        return [
            fmt.strip()
            for fmt in self.SUPPORTED_AUDIO_FORMATS.split(",")
        ]

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