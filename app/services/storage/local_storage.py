from pathlib import Path
import shutil

from app.services.storage.storage import (
    Storage,
)


class LocalStorage(Storage):

    def __init__(
        self,
        base_path: str = "data/raw",
    ):
        self.base_path = Path(base_path)

        self.base_path.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save_audio(
        self,
        source_path: str,
        file_name: str,
    ) -> str:

        destination = (
            self.base_path / file_name
        )

        shutil.copy2(
            source_path,
            destination,
        )

        return str(destination)

    def get_audio_path(
        self,
        file_name: str,
    ) -> str:

        return str(
            self.base_path / file_name
        )