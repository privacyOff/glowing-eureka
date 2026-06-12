from dataclasses import dataclass


@dataclass
class SentimentResult:
    positive: float
    neutral: float
    negative: float
    compound: float
    label: str