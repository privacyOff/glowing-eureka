import faiss
import numpy as np

from app.core.model_registry import (
    ModelRegistry,
)

from app.embeddings.schemas import (
    EmbeddingResult,
)


class EmbeddingService:

    def __init__(
        self,
    ) -> None:

        self.model = (
            ModelRegistry.embedding_model
        )

    def embed_text(
        self,
        text: str,
    ) -> EmbeddingResult:

        vector = self.model.encode(
            text,
            convert_to_numpy=True,
        )

        vector = (
            vector.astype("float32")
        )

        faiss.normalize_L2(
            vector.reshape(1, -1)
        )

        return EmbeddingResult(
            vector=vector,
            dimension=len(vector),
        )

    def embed_call(
        self,
        call,
        builder,
    ) -> EmbeddingResult:

        document = builder.build(
            call
        )

        return self.embed_text(
            document
        )