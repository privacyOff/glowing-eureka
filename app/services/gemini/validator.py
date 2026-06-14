from app.services.gemini.schemas import (
    SummaryResult,
    RootCauseResult,
    CustomerInsightResult,
)

class GeminiValidator:
    @staticmethod
    def validate_summary(
        data: dict,
    ) -> SummaryResult:

        return SummaryResult(
            **data
        )
    
    @staticmethod
    def validate_root_cause(
        data: dict,
    ) -> RootCauseResult:

        return RootCauseResult(
            **data
        )
    
    @staticmethod
    def validate_insights(
        data: dict,
    ) -> CustomerInsightResult:

        return (
            CustomerInsightResult(
                **data
            )
        )