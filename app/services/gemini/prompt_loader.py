from pathlib import Path


class PromptLoader:

    @staticmethod
    def load(
        filename: str,
    ) -> str:

        path = (
            Path("app/prompts")
            / filename
        )

        return path.read_text(
            encoding="utf-8"
        )