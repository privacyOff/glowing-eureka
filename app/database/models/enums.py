from enum import Enum


class ProcessingStatus(str, Enum):
    UPLOADED = "uploaded"
    TRANSCRIBED = "transcribed"
    PROCESSED = "processed"
    FAILED = "failed"