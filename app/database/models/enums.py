from enum import Enum


class ProcessingStatus(str, Enum):
    UPLOADED = "uploaded"

    TRANSCRIBING = "transcribing"

    TRANSCRIBED = "transcribed"

    ANALYZING = "analyzing"

    EMBEDDING = "embedding"

    COMPLETED = "completed"

    FAILED = "failed"