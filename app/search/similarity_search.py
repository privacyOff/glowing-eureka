import time

from sqlalchemy.orm import Session

from app.config.settings import (
    settings,
)

from app.embeddings.embedding_service import (
    EmbeddingService,
)

from app.search.faiss_store import (
    FAISSStore,
)

from app.search.schemas import (
    SearchResult,
    SemanticSearchResponse,
)

from app.database.repositories.call_repository import (
    CallRepository,
)

from app.database.repositories.search_repository import (
    SearchRepository,
)


class SimilarityService:

    def __init__(
        self,
        db: Session,
    ) -> None:

        self.db = db

        self.embedding_service = (
            EmbeddingService()
        )

        self.faiss_store = (
            FAISSStore()
        )

        self.faiss_store.load()

        self.call_repository = (
            CallRepository(db)
        )

        self.search_repository = (
            SearchRepository(db)
        )

    def search(
        self,
        query: str,
    ) -> SemanticSearchResponse:

        start = time.time()

        query_embedding = (
            self.embedding_service
            .embed_text(query)
        )

        scores, indices = (
            self.faiss_store.search(
                query_embedding.vector,
                top_k=settings.SEARCH_TOP_K,
            )
        )

        results = []

        for score, idx in zip(
            scores,
            indices,
        ):

            if idx == -1:
                continue

            call_id = (
                self.faiss_store
                .metadata[idx]
            )

            call = (
                self.call_repository
                .get_by_id(call_id)
            )

            if not call:
                continue

            category = None

            if call.categories:

                category = (
                    call.categories[0]
                    .category
                )

            results.append(
                SearchResult(
                    call_id=str(
                        call.call_id
                    ),
                    similarity_score=float(
                        score
                    ),
                    category=category,
                    summary=call.summary,
                )
            )

        latency_ms = (
            time.time() - start
        ) * 1000

        self.search_repository.create(
            query=query,
            result_count=len(results),
            latency_ms=latency_ms,
        )

        return (
            SemanticSearchResponse(
                results=results
            )
        )