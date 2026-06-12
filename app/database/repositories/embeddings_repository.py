from uuid import UUID

from app.database.models.embedding import (
    CallEmbedding,
)
from app.database.repositories.base_repository import (
    BaseRepository,
)


class EmbeddingRepository(BaseRepository):

    def create(
        self,
        embedding: CallEmbedding,
    ) -> CallEmbedding:

        self.db.add(embedding)
        self.db.commit()
        self.db.refresh(embedding)

        return embedding

    def get_by_call_id(
        self,
        call_id: UUID,
    ) -> list[CallEmbedding]:

        return (
            self.db.query(CallEmbedding)
            .filter(CallEmbedding.call_id == call_id)
            .all()
        )