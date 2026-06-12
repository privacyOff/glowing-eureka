import re

from app.services.ner.schemas import (
    EntityResult,
)

ORDER_ID_PATTERN = (
    r"\b(?:ORD|ORDER)-?\d+\b"
)

TRACKING_PATTERN = (
    r"\b(?:TRK|TRACK)-?\d+\b"
)

INVOICE_PATTERN = (
    r"\b(?:INV|INVOICE)-?\d+\b"
)

ACCOUNT_PATTERN = (
    r"\b(?:ACC|ACCOUNT)-?\d+\b"
)

class RegexExtractor:

    def extract(
        self,
        text: str,
    ) -> list[EntityResult]:

        entities = []

        entities.extend(
            self._find(
                text,
                ORDER_ID_PATTERN,
                "ORDER_ID",
            )
        )

        entities.extend(
            self._find(
                text,
                TRACKING_PATTERN,
                "TRACKING_NUMBER",
            )
        )

        entities.extend(
            self._find(
                text,
                INVOICE_PATTERN,
                "INVOICE_ID",
            )
        )

        entities.extend(
            self._find(
                text,
                ACCOUNT_PATTERN,
                "ACCOUNT_NUMBER",
            )
        )

        return entities

    def _find(
        self,
        text: str,
        pattern: str,
        label: str,
    ):

        results = []

        for match in re.finditer(
            pattern,
            text,
            flags=re.IGNORECASE,
        ):

            results.append(
                EntityResult(
                    text=match.group(),
                    label=label,
                    start=match.start(),
                    end=match.end(),
                    confidence=None,
                )
            )

        return results

