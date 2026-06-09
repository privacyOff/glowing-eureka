"""
Application-wide constants.
"""

SUPPORTED_WHISPER_MODELS = {
    "tiny",
    "base",
    "small",
    "medium",
    "large",
}

SUPPORTED_EMBEDDING_MODELS = {
    "all-MiniLM-L6-v2",
    "bge-small-en-v1.5",
    "bge-base-en-v1.5",
    "e5-base-v2",
}

DEFAULT_LOG_LEVEL = "INFO"

DEFAULT_FAISS_FILENAME = "faiss.index"

DEFAULT_METADATA_FILENAME = "metadata.pkl"