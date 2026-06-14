from app.core.model_registry import (
    ModelRegistry,
)

from app.config.classification_categories import (
    CATEGORIES,
)

class ZeroShotClassifier:

    def __init__(self):

        self.model = (
            ModelRegistry.classification_model
        )

    def classify(
        self,
        transcript: str,
    ):

        return self.model(
            transcript,
            candidate_labels=CATEGORIES,
            multi_label=False,
        )