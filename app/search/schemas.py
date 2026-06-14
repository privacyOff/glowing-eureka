from dataclasses import dataclass


@dataclass
class SearchResult:
    call_id: str
    similarity_score: float
    category: str | None = None
    summary: str | None = None


@dataclass
class SemanticSearchResponse:
    results: list[SearchResult]