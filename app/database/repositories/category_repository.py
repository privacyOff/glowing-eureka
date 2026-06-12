from uuid import UUID

from app.database.models.category import (
    CallCategory,
)
from app.database.repositories.base_repository import (
    BaseRepository,
)


class CategoryRepository(BaseRepository):

    def create(
        self,
        category: CallCategory,
    ) -> CallCategory:

        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)

        return category

    def bulk_create(
        self,
        categories: list[CallCategory],
    ) -> None:

        self.db.add_all(categories)
        self.db.commit()

    def get_by_call_id(
        self,
        call_id: UUID,
    ) -> list[CallCategory]:

        return (
            self.db.query(CallCategory)
            .filter(CallCategory.call_id == call_id)
            .all()
        )