from uuid import UUID

from app.database.models.entity import Entity
from app.database.repositories.base_repository import (
    BaseRepository,
)


class EntityRepository(BaseRepository):

    def create(
        self,
        entity: Entity,
    ) -> Entity:

        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)

        return entity

    def bulk_create(
        self,
        entities: list[Entity],
    ) -> None:

        self.db.add_all(entities)
        self.db.commit()

    def get_by_call_id(
        self,
        call_id: UUID,
    ) -> list[Entity]:

        return (
            self.db.query(Entity)
            .filter(Entity.call_id == call_id)
            .all()
        )