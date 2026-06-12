import time

from app.config.settings import settings
from app.core.model_registry import (
    ModelRegistry,
)
from app.monitoring.events import (
    PipelineEvents,
)
from app.monitoring.logger import (
    get_logger,
)
from app.services.transcription.audio_validator import (
    AudioValidator,
)
from app.services.transcription.exceptions import (
    TranscriptionError,
)
from app.services.transcription.schemas import (
    TranscriptionResult,
)

logger = get_logger(
    "transcription"
)


class TranscriptionService:
    """
    Handles audio validation and transcription.

    This service does NOT perform any database
    operations. Persistence is handled by the
    repository layer.
    """

    def __init__(
        self,
    ) -> None:
        self.validator = (
            AudioValidator()
        )

        self.model = (
            ModelRegistry.whisper_model
        )

    def transcribe(
        self,
        audio_path: str,
        call_id: str | None = None,
    ) -> tuple:
        metadata = (
            self.validator.validate(
                audio_path
            )
        )

        logger.info(
            event=PipelineEvents.TRANSCRIPTION_STARTED,
            message="Transcription started",
            call_id=call_id,
            status="success",
        )

        try:
            start = (
                time.perf_counter()
            )

            result = (
                self.model.transcribe(
                    audio_path
                )
            )

            duration_ms = round(
                (
                    time.perf_counter()
                    - start
                )
                * 1000,
                2,
            )

            logger.info(
                event=PipelineEvents.TRANSCRIPTION_FINISHED,
                message="Transcription finished",
                call_id=call_id,
                status="success",
                duration_ms=duration_ms,
            )

            transcription_result = (
                TranscriptionResult(
                    transcript=result[
                        "text"
                    ].strip(),
                    language=result.get(
                        "language",
                        "unknown",
                    ),
                    duration_ms=duration_ms,
                    whisper_model=settings.WHISPER_MODEL,
                )
            )

            return (
                metadata,
                transcription_result,
            )

        except Exception as e:
            logger.error(
                event=PipelineEvents.TRANSCRIPTION_FAILED,
                message="Transcription failed",
                call_id=call_id,
                status="failed",
                error_type=type(
                    e
                ).__name__,
                error_message=str(e),
            )

            raise TranscriptionError(
                str(e)
            ) from e