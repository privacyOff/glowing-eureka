import time


class RetryPolicy:

    def execute(
        self,
        func,
        retries: int = 3,
    ):

        last_error = None

        for attempt in range(
            retries
        ):

            try:

                return func()

            except Exception as e:

                last_error = e

                time.sleep(
                    2**attempt
                )

        raise last_error