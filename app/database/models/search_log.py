import uuid
from datetime import datetime, timezone

from sqlalchemy import (
    DateTime,
    Float,
    Index,
    Integer,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.database.base import Base


class SearchLog(Base):
    __tablename__ = "search_logs"

    __table_args__ = (
        Index("idx_search_logs_timestamp", "timestamp"),
        Index("idx_search_logs_user_id", "user_id"),
    )

    search_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    user_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    query: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
    )

    result_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    latency_ms: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )