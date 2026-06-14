from app.config.settings import (
    settings,
)

from app.monitoring.logger import (
    get_logger,
)

from app.monitoring.events import (
    PipelineEvents,
)

from app.config.classification_categories import (
    FALLBACK_CATEGORY,
)

from app.services.classification.schemas import (
    CategoryPrediction,
    ClassificationResult,
)

from app.services.classification.classifier import (
    ZeroShotClassifier,
)

from app.services.classification.exceptions import (
    ClassificationError,
)

logger = get_logger(
    "classification"
)


class ClassificationService:

    def __init__(
        self,
    ) -> None:
        self.classifier = (
            ZeroShotClassifier()
        )

    def classify(
        self,
        transcript: str,
        call_id: str | None = None,
    ) -> ClassificationResult:

        logger.info(
            event=PipelineEvents.CLASSIFICATION_STARTED,
            message="Classification started",
            call_id=call_id,
            status="success",
        )

        try:

            result = (
                self.classifier.classify(
                    transcript
                )
            )

            prediction = (
                self._build_prediction(
                    result
                )
            )

            classification_result = (
                ClassificationResult(
                    predictions=[
                        prediction
                    ]
                )
            )

            logger.info(
                event=PipelineEvents.CLASSIFICATION_COMPLETED,
                message="Classification completed",
                call_id=call_id,
                status="success",
            )

            return classification_result

        except Exception as e:

            logger.error(
                event=PipelineEvents.CLASSIFICATION_FAILED,
                message="Classification failed",
                call_id=call_id,
                status="failed",
                error_type=type(e).__name__,
                error_message=str(e),
            )

            raise ClassificationError(
                str(e)
            ) from e

    def _build_prediction(
        self,
        result: dict,
    ) -> CategoryPrediction:

        category = (
            result["labels"][0]
        )

        confidence = float(
            result["scores"][0]
        )

        if (
            confidence
            < settings.CLASSIFICATION_THRESHOLD
        ):
            return CategoryPrediction(
                category=FALLBACK_CATEGORY,
                confidence=confidence,
            )

        return CategoryPrediction(
            category=category,
            confidence=confidence,
        )