from app.config.settings import (
    settings,
)

from app.monitoring.logger import (
    get_logger,
)

from app.monitoring.events import (
    PipelineEvents,
)

from app.services.ner.schemas import (
    NERResult,
)

from app.services.ner.exceptions import (
    NERExtractionError,
)

from app.services.ner.spacy_analyzer import (
    SpacyAnalyzer,
)

from app.services.ner.custom_extractors import (
    RegexExtractor,
)

logger = get_logger("ner")

class NERService:

    def __init__(self):

        self.spacy_analyzer = (
            SpacyAnalyzer()
        )

        self.regex_extractor = (
            RegexExtractor()
        )

    def extract(
        self,
        transcript: str,
        call_id: str | None = None,
    ) -> NERResult:

        logger.info(
            event=PipelineEvents.NER_STARTED,
            message="NER extraction started",
            call_id=call_id,
            status="success",
        )

        try:

            entities = []

            entities.extend(
                self.spacy_analyzer.extract(
                    transcript
                )
            )

            if (
                settings.ENABLE_REGEX_ENTITIES
            ):
                entities.extend(
                    self.regex_extractor.extract(
                        transcript
                    )
                )

            result = NERResult(
                entities=entities
            )

            logger.info(
                event=PipelineEvents.NER_COMPLETED,
                message="NER extraction completed",
                call_id=call_id,
                status="success",
            )

            return result

        except Exception as e:

            logger.error(
                event=PipelineEvents.NER_FAILED,
                message="NER extraction failed",
                call_id=call_id,
                status="failed",
                error_type=type(
                    e
                ).__name__,
                error_message=str(e),
            )

            raise NERExtractionError(
                str(e)
            )

