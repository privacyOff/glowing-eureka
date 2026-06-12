import uuid
from datetime import datetime, timezone

from sqlalchemy import (
    Boolean,
    DateTime,
    Enum,
    Float,
    Index,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import Base
from app.database.models.enums import ProcessingStatus


class Call(Base):
    __tablename__ = "calls"

    __table_args__ = (
        Index("idx_calls_created_at", "created_at"),
        Index("idx_calls_status", "processing_status"),
        Index("idx_calls_sentiment", "sentiment_label"),
    )

    call_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    file_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    file_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    transcript: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    sentiment_label: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    sentiment_score: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    processing_status: Mapped[ProcessingStatus] = mapped_column(
        Enum(ProcessingStatus),
        default=ProcessingStatus.UPLOADED,
        nullable=False,
    )

    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    categories: Mapped[list["CallCategory"]] = relationship(
        back_populates="call",
        cascade="all, delete-orphan",
    )

    entities: Mapped[list["Entity"]] = relationship(
        back_populates="call",
        cascade="all, delete-orphan",
    )

    embeddings: Mapped[list["CallEmbedding"]] = relationship(
        back_populates="call",
        cascade="all, delete-orphan",
    )