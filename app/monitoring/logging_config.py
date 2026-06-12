import json
import logging
from datetime import datetime
from pathlib import Path

from app.config.settings import settings


class JsonFormatter(logging.Formatter):

    def format(self, record):

        payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "service": getattr(
                record,
                "service",
                "application",
            ),
            "event": getattr(
                record,
                "event",
                None,
            ),
            "call_id": getattr(
                record,
                "call_id",
                None,
            ),
            "level": record.levelname,
            "status": getattr(
                record,
                "status",
                None,
            ),
            "duration_ms": getattr(
                record,
                "duration_ms",
                None,
            ),
            "message": record.getMessage(),
            "error_type": getattr(
                record,
                "error_type",
                None,
            ),
            "error_message": getattr(
                record,
                "error_message",
                None,
            ),
        }

        return json.dumps(payload)


def configure_logging():

    Path("logs").mkdir(
        parents=True,
        exist_ok=True,
    )

    formatter = JsonFormatter()

    root_logger = logging.getLogger()

    root_logger.setLevel(settings.LOG_LEVEL)

    root_logger.handlers.clear()

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        formatter
    )

    file_handler = logging.FileHandler(
        settings.LOG_PATH
    )
    file_handler.setFormatter(
        formatter
    )

    root_logger.addHandler(
        console_handler
    )

    root_logger.addHandler(
        file_handler
    )