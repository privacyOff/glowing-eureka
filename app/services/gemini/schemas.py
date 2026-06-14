from enum import Enum

from pydantic import BaseModel


class UrgencyLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class SummaryResult(BaseModel):

    issue_summary: str

    resolution_summary: str | None = None

    action_items: list[str]

class RootCauseResult(BaseModel):

    root_cause: str

    recurring_patterns: list[str]

class CustomerInsightResult(BaseModel):

    main_complaint: str

    pain_points: list[str]

    risk_indicators: list[str]

    urgency_level: UrgencyLevel