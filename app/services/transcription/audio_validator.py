from pathlib import Path

import ffmpeg
import whisper

from app.config.settings import settings
from app.services.transcription.exceptions import (
    AudioCorruptedError,
    AudioValidationError,
)
from app.services.transcription.schemas import (
    AudioMetadata,
)


class AudioValidator:
    """
    Validates audio files before transcription.
    """

    def validate(
        self,
        audio_path: str,
    ) -> AudioMetadata:
        self._validate_exists(
            audio_path
        )

        self._validate_extension(
            audio_path
        )

        metadata = (
            self._extract_metadata(
                audio_path
            )
        )

        self._validate_duration(
            metadata
        )

        self._validate_corruption(
            audio_path
        )

        return metadata

    def _validate_exists(
        self,
        audio_path: str,
    ) -> None:
        if not Path(audio_path).exists():
            raise AudioValidationError(
                f"File not found: {audio_path}"
            )

    def _validate_extension(
        self,
        audio_path: str,
    ) -> None:
        extension = (
            Path(audio_path)
            .suffix.lower()
            .replace(".", "")
        )

        if (
            extension
            not in settings.supported_audio_formats
        ):
            raise AudioValidationError(
                f"Unsupported format: {extension}"
            )

    def _extract_metadata(
        self,
        audio_path: str,
    ) -> AudioMetadata:
        try:
            probe = ffmpeg.probe(
                audio_path
            )

            audio_stream = next(
                stream
                for stream in probe["streams"]
                if stream["codec_type"]
                == "audio"
            )

            duration = float(
                probe["format"]["duration"]
            )

            sample_rate = int(
                audio_stream["sample_rate"]
            )

            channels = int(
                audio_stream["channels"]
            )

            file_size = Path(
                audio_path
            ).stat().st_size

            return AudioMetadata(
                duration_seconds=duration,
                sample_rate=sample_rate,
                channels=channels,
                file_size_bytes=file_size,
            )

        except Exception as e:
            raise AudioValidationError(
                f"Failed to extract metadata: {e}"
            ) from e

    def _validate_duration(
        self,
        metadata: AudioMetadata,
    ) -> None:
        max_duration = (
            settings.MAX_AUDIO_DURATION_MINUTES
            * 60
        )

        if (
            metadata.duration_seconds
            > max_duration
        ):
            raise AudioValidationError(
                "Audio exceeds maximum duration"
            )

    def _validate_corruption(
        self,
        audio_path: str,
    ) -> None:
        try:
            whisper.load_audio(
                audio_path
            )

        except Exception as e:
            raise AudioCorruptedError(
                str(e)
            ) from e