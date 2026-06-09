from pathlib import Path

from app.config.constants import (
    SUPPORTED_EMBEDDING_MODELS,
    SUPPORTED_WHISPER_MODELS,
)
from app.config.settings import Settings


def validate_settings(settings: Settings) -> None:
    """
    Validate configuration values.
    """

    validate_whisper_model(settings)
    validate_embedding_model(settings)
    validate_paths(settings)


def validate_whisper_model(settings: Settings) -> None:
    if settings.WHISPER_MODEL not in SUPPORTED_WHISPER_MODELS:
        raise ValueError(
            f"Unsupported Whisper model: "
            f"{settings.WHISPER_MODEL}"
        )


def validate_embedding_model(settings: Settings) -> None:
    if settings.EMBEDDING_MODEL not in SUPPORTED_EMBEDDING_MODELS:
        raise ValueError(
            f"Unsupported embedding model: "
            f"{settings.EMBEDDING_MODEL}"
        )


def validate_paths(settings: Settings) -> None:
    """
    Validate path values.
    """

    if not settings.FAISS_PATH:
        raise ValueError("FAISS_PATH cannot be empty")

    if not settings.LOG_PATH:
        raise ValueError("LOG_PATH cannot be empty")

    Path(settings.FAISS_PATH)
    Path(settings.LOG_PATH)