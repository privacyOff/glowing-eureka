class PipelineEvents:
    # Success Events
    AUDIO_UPLOADED = "audio_uploaded"

    TRANSCRIPTION_STARTED = "transcription_started"
    TRANSCRIPTION_FINISHED = "transcription_finished"

    SENTIMENT_COMPLETED = "sentiment_completed"

    NER_STARTED = "ner_started"
    NER_COMPLETED = "ner_completed"

    CLASSIFICATION_COMPLETED = "classification_completed"

    EMBEDDING_GENERATED = "embedding_generated"

    SEARCH_EXECUTED = "search_executed"

    GEMINI_SUMMARY_GENERATED = (
        "gemini_summary_generated"
    )

    # Failure Events
    AUDIO_UPLOAD_FAILED = (
        "audio_upload_failed"
    )

    TRANSCRIPTION_FAILED = (
        "transcription_failed"
    )

    SENTIMENT_FAILED = (
        "sentiment_failed"
    )

    NER_FAILED = "ner_failed"

    CLASSIFICATION_FAILED = (
        "classification_failed"
    )

    EMBEDDING_FAILED = (
        "embedding_failed"
    )

    SEARCH_FAILED = "search_failed"

    GEMINI_SUMMARY_FAILED = (
        "gemini_summary_failed"
    )

    # Infrastructure Events
    APPLICATION_STARTED = (
        "application_started"
    )

    APPLICATION_STOPPED = (
        "application_stopped"
    )

    DATABASE_CONNECTED = (
        "database_connected"
    )

    DATABASE_CONNECTION_FAILED = (
        "database_connection_failed"
    )

    MODELS_LOADED = (
        "models_loaded"
    )

    MODEL_LOAD_FAILED = (
        "model_load_failed"
    )

    STARTUP_CHECKS_PASSED = (
        "startup_checks_passed"
    )

    STARTUP_CHECKS_FAILED = (
        "startup_checks_failed"
    )

    GEMINI_CONNECTED = (
        "gemini_connected"
    )

    GEMINI_CONNECTION_FAILED = (
        "gemini_connection_failed"
    )