from uuid import UUID

from app.database.models.call import Call
from app.database.models.enums import ProcessingStatus
from app.database.repositories.base_repository import (
    BaseRepository,
)


class CallRepository(BaseRepository):

    def create(
        self,
        call: Call,
    ) -> Call:

        self.db.add(call)
        self.db.commit()
        self.db.refresh(call)

        return call

    def get_by_id(
        self,
        call_id: UUID,
    ) -> Call | None:

        return (
            self.db.query(Call)
            .filter(Call.call_id == call_id)
            .first()
        )

    def get_all(self) -> list[Call]:

        return (
            self.db.query(Call)
            .order_by(Call.created_at.desc())
            .all()
        )

    def update_status(
        self,
        call_id: UUID,
        status: ProcessingStatus,
    ) -> bool:

        call = self.get_by_id(call_id)

        if not call:
            return False

        call.processing_status = status

        self.db.commit()

        return True

    def update_transcript(
        self,
        call_id: UUID,
        transcript: str,
        language: str,
        whisper_model: str,
        duration_ms: float,
    ) -> bool:

        call = self.get_by_id(call_id)

        if not call:
            return False

        call.transcript = transcript
        call.detected_language = language
        call.whisper_model = whisper_model
        call.transcription_duration_ms = duration_ms
        call.processing_status = (
            ProcessingStatus.TRANSCRIBED
        )

        self.db.commit()

        return True

    def update_summary(
        self,
        call_id: UUID,
        summary: str,
    ) -> bool:

        call = self.get_by_id(call_id)

        if not call:
            return False

        call.summary = summary

        self.db.commit()

        return True

    def update_sentiment(
        self,
        call_id: UUID,
        label: str,
        score: float,
    ) -> bool:

        call = self.get_by_id(call_id)

        if not call:
            return False

        call.sentiment_label = label
        call.sentiment_score = score

        self.db.commit()

        return True

    def soft_delete(
        self,
        call_id: UUID,
    ) -> bool:

        call = self.get_by_id(call_id)

        if not call:
            return False

        call.is_deleted = True

        self.db.commit()

        return True