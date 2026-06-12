import time
from functools import wraps

from app.monitoring.logger import (
    get_logger,
)


def track_duration(
    service: str,
    event: str,
):

    logger = get_logger(service)

    def decorator(func):

        @wraps(func)
        def wrapper(
            *args,
            **kwargs,
        ):

            start = time.perf_counter()

            try:

                result = func(
                    *args,
                    **kwargs,
                )

                duration_ms = round(
                    (
                        time.perf_counter()
                        - start
                    )
                    * 1000,
                    2,
                )

                logger.info(
                    event=event,
                    message="Operation completed",
                    duration_ms=duration_ms,
                    status="success",
                )

                return result

            except Exception as e:

                duration_ms = round(
                    (
                        time.perf_counter()
                        - start
                    )
                    * 1000,
                    2,
                )

                logger.error(
                    event=f"{event}_failed",
                    message="Operation failed",
                    duration_ms=duration_ms,
                    status="failed",
                    error_type=type(
                        e
                    ).__name__,
                    error_message=str(e),
                )

                raise

        return wrapper

    return decorator