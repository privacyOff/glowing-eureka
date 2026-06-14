from pathlib import Path

import spacy
import whisper
from google import generativeai as genai
from sentence_transformers import SentenceTransformer
from sqlalchemy import create_engine, text
from transformers import pipeline

from app.config.settings import Settings
from app.core.model_registry import ModelRegistry
from app.monitoring.events import PipelineEvents
from app.monitoring.logger import get_logger

logger = get_logger("startup")


def validate_configuration(
    settings: Settings,
) -> None:
    """
    Validate application configuration.
    """

    if settings.MAX_AUDIO_DURATION_MINUTES <= 0:
        raise ValueError(
            "MAX_AUDIO_DURATION_MINUTES must be greater than 0."
        )

    allowed_formats = {
        "wav",
        "mp3",
        "m4a",
        "flac",
    }

    configured_formats = {
        fmt.lower()
        for fmt in settings.supported_audio_formats
    }

    if not configured_formats:
        raise ValueError(
            "SUPPORTED_AUDIO_FORMATS cannot be empty."
        )

    invalid_formats = (
        configured_formats - allowed_formats
    )

    if invalid_formats:
        raise ValueError(
            "Unsupported audio formats configured: "
            f"{', '.join(sorted(invalid_formats))}"
        )

    logger.info(
        event=PipelineEvents.STARTUP_CHECKS_PASSED,
        message="Configuration validation passed",
        status="success",
    )


def create_directories(
    settings: Settings,
) -> None:
    """
    Create required directories.
    """

    directories = [
        settings.FAISS_PATH,
        "data/transcripts",
        "data/processed",
        "logs",
    ]

    for directory in directories:
        Path(directory).mkdir(
            parents=True,
            exist_ok=True,
        )


def check_database(
    settings: Settings,
) -> None:
    try:
        engine = create_engine(
            settings.DATABASE_URL
        )

        with engine.connect() as connection:
            connection.execute(
                text("SELECT 1")
            )

        logger.info(
            event=PipelineEvents.DATABASE_CONNECTED,
            message="Database connection established",
            status="success",
        )

    except Exception as e:
        logger.error(
            event=PipelineEvents.DATABASE_CONNECTION_FAILED,
            message="Database connection failed",
            status="failed",
            error_type=type(e).__name__,
            error_message=str(e),
        )
        raise


def check_gemini(
    settings: Settings,
) -> None:
    """
    Verify Gemini availability.
    """

    if not settings.GEMINI_API_KEY:

        if settings.REQUIRE_GEMINI:
            raise RuntimeError(
                "GEMINI_API_KEY is required."
            )

        logger.warning(
            event=PipelineEvents.GEMINI_DISABLED,
            message="Gemini key missing",
            status="disabled",
        )
        return

    try:
        genai.configure(
            api_key=settings.GEMINI_API_KEY
        )

        list(genai.list_models())

    except Exception as e:

        if settings.REQUIRE_GEMINI:
            raise RuntimeError(
                f"Gemini unavailable: {e}"
            )

        logger.warning(
            event=PipelineEvents.GEMINI_UNAVAILABLE,
            message="Gemini unavailable",
            status="warning",
            error_type=type(e).__name__,
            error_message=str(e),
        )


def preload_whisper(
    settings: Settings,
) -> None:
    """
    Load Whisper model.
    """

    ModelRegistry.whisper_model = (
        whisper.load_model(
            settings.WHISPER_MODEL
        )
    )

    logger.info(
        event=PipelineEvents.MODELS_LOADED,
        message=f"Loaded Whisper model: {settings.WHISPER_MODEL}",
        status="success",
    )


def preload_embedding_model(
    settings: Settings,
) -> None:
    """
    Load embedding model.
    """

    ModelRegistry.embedding_model = (
        SentenceTransformer(
            settings.EMBEDDING_MODEL
        )
    )

    logger.info(
        event=PipelineEvents.MODELS_LOADED,
        message=f"Loaded embedding model: {settings.EMBEDDING_MODEL}",
        status="success",
    )


def preload_ner_model(
    settings: Settings,
) -> None:
    """
    Load NER model.
    """

    ModelRegistry.ner_model = (
        spacy.load(
            settings.NER_MODEL
        )
    )

    logger.info(
        event=PipelineEvents.MODELS_LOADED,
        message=f"Loaded NER model: {settings.NER_MODEL}",
        status="success",
    )


def preload_classification_model(
    settings: Settings,
) -> None:
    """
    Load zero-shot classification model.
    """

    ModelRegistry.classification_model = (
        pipeline(
            task="zero-shot-classification",
            model=settings.CLASSIFICATION_MODEL,
        )
    )

    logger.info(
        event=PipelineEvents.MODELS_LOADED,
        message=(
            f"Loaded classification model: "
            f"{settings.CLASSIFICATION_MODEL}"
        ),
        status="success",
    )


def run_startup_checks(
    settings: Settings,
) -> None:
    validate_configuration(
        settings
    )

    create_directories(
        settings
    )

    check_database(
        settings
    )

    check_gemini(
        settings
    )

    preload_whisper(
        settings
    )

    preload_embedding_model(
        settings
    )

    preload_ner_model(
        settings
    )

    preload_classification_model(
        settings
    )

    logger.info(
        event=PipelineEvents.STARTUP_CHECKS_PASSED,
        message="Startup checks completed",
        status="success",
    )