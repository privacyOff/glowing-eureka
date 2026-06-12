from pathlib import Path

import whisper
from google import generativeai as genai
from sentence_transformers import SentenceTransformer
from sqlalchemy import create_engine, text

from app.config.settings import Settings
from app.core.model_registry import ModelRegistry

from app.monitoring.logger import get_logger
from app.monitoring.events import PipelineEvents

logger = get_logger("startup")


def create_directories(settings: Settings) -> None:
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


def check_database(settings: Settings) -> None:
    try:
        engine = create_engine(settings.DATABASE_URL)

        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

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


def check_gemini(settings: Settings) -> None:
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


def preload_whisper(settings: Settings) -> None:
    """
    Load Whisper model.
    """

    ModelRegistry.whisper_model = (
        whisper.load_model(
            settings.WHISPER_MODEL
        )
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


def run_startup_checks(
    settings: Settings,
) -> None:
    create_directories(settings)

    check_database(settings)

    check_gemini(settings)

    preload_whisper(settings)

    preload_embedding_model(settings)

    logger.info(
        event=PipelineEvents.STARTUP_CHECKS_PASSED,
        message="Startup checks completed",
        status="success",
    )