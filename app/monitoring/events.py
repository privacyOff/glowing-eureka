class PipelineEvents:
    # Success Events
    AUDIO_UPLOADED = "audio_uploaded"

    TRANSCRIPTION_STARTED = (
        "transcription_started"
    )

    TRANSCRIPTION_FINISHED = (
        "transcription_finished"
    )

    SENTIMENT_COMPLETED = (
        "sentiment_completed"
    )

    NER_STARTED = "ner_started"

    NER_COMPLETED = (
        "ner_completed"
    )

    CLASSIFICATION_STARTED = (
        "classification_started"
    )

    CLASSIFICATION_COMPLETED = (
        "classification_completed"
    )

    EMBEDDING_GENERATED = (
        "embedding_generated"
    )

    SEARCH_EXECUTED = (
        "search_executed"
    )

    # Gemini Summary Events
    GEMINI_SUMMARY_STARTED = (
        "gemini_summary_started"
    )

    GEMINI_SUMMARY_COMPLETED = (
        "gemini_summary_completed"
    )

    # Gemini Root Cause Events
    GEMINI_ROOT_CAUSE_STARTED = (
        "gemini_root_cause_started"
    )

    GEMINI_ROOT_CAUSE_COMPLETED = (
        "gemini_root_cause_completed"
    )

    # Gemini Insights Events
    GEMINI_INSIGHTS_STARTED = (
        "gemini_insights_started"
    )

    GEMINI_INSIGHTS_COMPLETED = (
        "gemini_insights_completed"
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

    NER_FAILED = (
        "ner_failed"
    )

    CLASSIFICATION_FAILED = (
        "classification_failed"
    )

    EMBEDDING_FAILED = (
        "embedding_failed"
    )

    SEARCH_FAILED = (
        "search_failed"
    )

    GEMINI_SUMMARY_FAILED = (
        "gemini_summary_failed"
    )

    GEMINI_ROOT_CAUSE_FAILED = (
        "gemini_root_cause_failed"
    )

    GEMINI_INSIGHTS_FAILED = (
        "gemini_insights_failed"
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