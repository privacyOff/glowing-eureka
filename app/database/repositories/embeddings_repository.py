from uuid import UUID

from app.config.settings import (
    settings,
)

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

    def create_embedding_record(
        self,
        call_id,
        embedding_model,
        dimension,
    ) -> CallEmbedding:

        embedding = (
            CallEmbedding(
                call_id=call_id,
                embedding_model=
                    embedding_model,
                vector_path=
                    settings.FAISS_INDEX_FILE,
                dimension=
                    dimension,
            )
        )

        self.db.add(
            embedding
        )

        self.db.commit()

        self.db.refresh(
            embedding
        )

        return embedding

    def get_by_call_id(
        self,
        call_id: UUID,
    ) -> list[CallEmbedding]:

        return (
            self.db.query(CallEmbedding)
            .filter(
                CallEmbedding.call_id == call_id
            )
            .all()
        )