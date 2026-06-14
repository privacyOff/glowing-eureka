import uuid
from datetime import datetime, timezone

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    JSON,
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import Base


class CallInsight(Base):
    __tablename__ = "call_insights"

    insight_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    call_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("calls.call_id"),
        nullable=False,
    )

    issue_summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    resolution_summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    root_cause: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    recurring_patterns: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    main_complaint: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    pain_points: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    risk_indicators: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    urgency_level: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    generation_status: Mapped[str] = mapped_column(
        String(50),
        default="completed",
    )

    prompt_version: Mapped[str] = mapped_column(
        String(100),
    )

    model_name: Mapped[str] = mapped_column(
        String(255),
    )

    insight_version: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )