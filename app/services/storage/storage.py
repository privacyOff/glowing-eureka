from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def save_audio(
        self,
        source_path: str,
        file_name: str,
    ) -> str:
        pass

    @abstractmethod
    def get_audio_path(
        self,
        file_name: str,
    ) -> str:
        pass