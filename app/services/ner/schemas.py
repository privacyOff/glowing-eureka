from dataclasses import dataclass


@dataclass
class EntityResult:
    text: str
    label: str
    start: int
    end: int
    confidence: float | None = None


@dataclass
class NERResult:
    entities: list[EntityResult]