from app.services.gemini.prompt_loader import PromptLoader
from app.services.gemini.retry_policy import RetryPolicy
from app.services.gemini.validator import GeminiValidator
from app.services.gemini.gemini_client import GeminiClient

from app.schemas.summary import SummaryResult
from app.schemas.root_cause import RootCauseResult
from app.schemas.customer_insight import CustomerInsightResult


class GeminiService:
    def __init__(self):
        self.client = GeminiClient()
        self.retry_policy = RetryPolicy()

    def _generate(
        self,
        transcript: str,
        prompt_file: str,
        validator,
    ):
        prompt_template = PromptLoader.load(prompt_file)

        prompt = prompt_template.replace(
            "{{transcript}}",
            transcript,
        )

        result = self.retry_policy.execute(
            lambda: self.client.generate_json(prompt)
        )

        return validator(result)

    def generate_summary(
        self,
        transcript: str,
    ) -> SummaryResult:
        return self._generate(
            transcript=transcript,
            prompt_file="summary_v1.txt",
            validator=GeminiValidator.validate_summary,
        )

    def generate_root_cause(
        self,
        transcript: str,
    ) -> RootCauseResult:
        return self._generate(
            transcript=transcript,
            prompt_file="root_cause_v1.txt",
            validator=GeminiValidator.validate_root_cause,
        )

    def generate_customer_insights(
        self,
        transcript: str,
    ) -> CustomerInsightResult:
        return self._generate(
            transcript=transcript,
            prompt_file="customer_insights_v1.txt",
            validator=GeminiValidator.validate_customer_insights,
        )