from app.core.model_registry import (
    ModelRegistry,
)

from app.services.ner.schemas import (
    EntityResult,
)

SUPPORTED_ENTITY_TYPES = {
    "PERSON",
    "ORG",
    "DATE",
    "MONEY",
    "PRODUCT",
    "GPE",
}

class SpacyAnalyzer:

    def __init__(self):

        self.nlp = (
            ModelRegistry.ner_model
        )

    def extract(
        self,
        text: str,
    ) -> list[EntityResult]:

        doc = self.nlp(text)

        entities = []

        for ent in doc.ents:

            if (
                ent.label_
                not in SUPPORTED_ENTITY_TYPES
            ):
                continue

            entities.append(
                EntityResult(
                    text=ent.text,
                    label=ent.label_,
                    start=ent.start_char,
                    end=ent.end_char,
                    confidence=None,
                )
            )

        return entities