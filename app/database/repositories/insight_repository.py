from app.database.models.call_insight import (
    CallInsight,
)


class InsightRepository:

    def __init__(self, db):
        self.db = db

    def create(
        self,
        **kwargs,
    ) -> CallInsight:

        insight = CallInsight(
            **kwargs
        )

        self.db.add(insight)

        self.db.commit()

        self.db.refresh(insight)

        return insight