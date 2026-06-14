from dataclasses import dataclass


@dataclass
class CategoryPrediction:
    category: str
    confidence: float


@dataclass
class ClassificationResult:
    predictions: list[CategoryPrediction]