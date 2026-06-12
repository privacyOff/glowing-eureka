from app.database.base import Base
from app.database.session import engine

# Register all models
from app.database.models import *


def init_db() -> None:
    Base.metadata.create_all(bind=engine)