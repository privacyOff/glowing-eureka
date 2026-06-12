from app.database.models.search_log import (
    SearchLog,
)
from app.database.repositories.base_repository import (
    BaseRepository,
)


class SearchLogRepository(BaseRepository):

    def create(
        self,
        log: SearchLog,
    ) -> SearchLog:

        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)

        return log