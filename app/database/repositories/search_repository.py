from app.database.models.search_log import (
    SearchLog,
)

from app.database.repositories.base_repository import (
    BaseRepository,
)


class SearchRepository(BaseRepository):

    def create(
        self,
        query,
        result_count,
        latency_ms,
        user_id=None,
    ) -> SearchLog:

        log = SearchLog(
            query=query,
            result_count=result_count,
            latency_ms=latency_ms,
            user_id=user_id,
        )

        self.db.add(
            log
        )

        self.db.commit()

        self.db.refresh(
            log
        )

        return log