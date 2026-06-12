from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
)

class NEREvaluator:

    def evaluate(
        self,
        y_true,
        y_pred,
    ):

        return {
            "precision": precision_score(
                y_true,
                y_pred,
                average="weighted",
            ),
            "recall": recall_score(
                y_true,
                y_pred,
                average="weighted",
            ),
            "f1": f1_score(
                y_true,
                y_pred,
                average="weighted",
            ),
        }