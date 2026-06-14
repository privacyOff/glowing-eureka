from pathlib import Path
import json
import pickle

import faiss

from app.config.settings import (
    settings,
)


class FAISSStore:

    def __init__(
        self,
    ) -> None:

        self.index_path = Path(
            settings.FAISS_INDEX_FILE
        )

        self.metadata_path = Path(
            settings.FAISS_METADATA_FILE
        )

        self.index_metadata_path = Path(
            settings.FAISS_INDEX_METADATA_FILE
        )

        self.dimension = 384

    def create_index(
        self,
    ) -> None:

        self.index = faiss.IndexFlatIP(
            self.dimension
        )

        self.metadata = {}

    def load(
        self,
    ) -> None:

        if not self.index_path.exists():

            self.create_index()

            return

        self.index = faiss.read_index(
            str(self.index_path)
        )

        with open(
            self.metadata_path,
            "rb",
        ) as f:

            self.metadata = pickle.load(
                f
            )

    def save(
        self,
    ) -> None:

        faiss.write_index(
            self.index,
            str(self.index_path),
        )

        with open(
            self.metadata_path,
            "wb",
        ) as f:

            pickle.dump(
                self.metadata,
                f,
            )

        self._save_index_metadata()

    def _save_index_metadata(
        self,
    ) -> None:

        metadata = {
            "version": "v1",
            "embedding_model":
                settings.EMBEDDING_MODEL,
            "dimension":
                self.dimension,
            "call_count":
                len(self.metadata),
        }

        with open(
            self.index_metadata_path,
            "w",
        ) as f:

            json.dump(
                metadata,
                f,
                indent=2,
            )

    def add_call(
        self,
        call_id,
        vector,
    ) -> None:

        idx = len(
            self.metadata
        )

        self.index.add(
            vector.reshape(1, -1)
        )

        self.metadata[idx] = str(
            call_id
        )

        self.save()

    def search(
        self,
        query_vector,
        top_k,
    ):

        scores, indices = (
            self.index.search(
                query_vector.reshape(1, -1),
                top_k,
            )
        )

        return (
            scores[0],
            indices[0],
        )