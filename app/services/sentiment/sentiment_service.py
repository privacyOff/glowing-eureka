# imports

from app.config.settings import settings

from app.monitoring.logger import (
    get_logger,
)

from app.monitoring.events import (
    PipelineEvents,
)

from app.services.sentiment.schemas import (
    SentimentResult,
)

from app.services.sentiment.exceptions import (
    SentimentAnalysisError,
)

from app.services.sentiment.vader_analyzer import (
    VaderAnalyzer,
)


# logger

logger = get_logger(
    "sentiment"
)


# service

class SentimentService:

    def __init__(self):

        self.analyzer = (
            VaderAnalyzer()
        )

    def analyze(
        self,
        transcript: str,
        call_id: str | None = None,
    ) -> SentimentResult:

        ...

    def _map_sentiment(
        self,
        compound: float,
    ) -> str:

        if (
            compound
            >= settings.SENTIMENT_POSITIVE_THRESHOLD
        ):
            return "positive"

        if (
            compound
            <= settings.SENTIMENT_NEGATIVE_THRESHOLD
        ):
            return "negative"

        return "neutral"