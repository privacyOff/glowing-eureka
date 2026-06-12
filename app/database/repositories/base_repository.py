from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, db: Session):
        self.db = db

    def add(self, obj):
        self.db.add(obj)
        return obj

    def add_all(self, objs):
        self.db.add_all(objs)

    def commit(self):
        self.db.commit()

    def refresh(self, obj):
        self.db.refresh(obj)

    def flush(self):
        self.db.flush()