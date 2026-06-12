from dataclasses import dataclass


@dataclass
class AudioMetadata:
    duration_seconds: float
    sample_rate: int
    channels: int
    file_size_bytes: int


@dataclass
class TranscriptionResult:
    transcript: str
    language: str
    duration_ms: float
    whisper_model: str