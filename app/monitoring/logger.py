import logging


class AppLogger:

    def __init__(
        self,
        service: str,
    ):
        self.logger = logging.getLogger(
            service
        )
        self.service = service

    def info(
        self,
        event: str,
        message: str,
        **kwargs,
    ):

        self.logger.info(
            message,
            extra={
                "service": self.service,
                "event": event,
                **kwargs,
            },
        )

    def error(
        self,
        event: str,
        message: str,
        **kwargs,
    ):

        self.logger.error(
            message,
            extra={
                "service": self.service,
                "event": event,
                **kwargs,
            },
        )

    def warning(
        self,
        event: str,
        message: str,
        **kwargs,
    ):

        self.logger.warning(
            message,
            extra={
                "service": self.service,
                "event": event,
                **kwargs,
            },
        )


def get_logger(
    service: str,
):

    return AppLogger(service)