from pathlib import Path

import whisper
from google import generativeai as genai
from sentence_transformers import SentenceTransformer
from sqlalchemy import create_engine, text

from app.config.settings import Settings
from app.core.model_registry import ModelRegistry


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
    """
    Verify database connectivity.
    """

    engine = create_engine(settings.DATABASE_URL)

    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))


def check_gemini(settings: Settings) -> None:
    """
    Verify Gemini availability.
    """

    if not settings.GEMINI_API_KEY:

        if settings.REQUIRE_GEMINI:
            raise RuntimeError(
                "GEMINI_API_KEY is required."
            )

        print(
            "[WARNING] Gemini key missing. "
            "Gemini features disabled."
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

        print(
            f"[WARNING] Gemini unavailable: {e}"
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
    """
    Execute startup sequence.
    """

    create_directories(settings)

    check_database(settings)

    check_gemini(settings)

    preload_whisper(settings)

    preload_embedding_model(settings)