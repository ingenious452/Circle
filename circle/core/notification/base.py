from abc import ABC, abstractmethod


class Notification(ABC):
    """
    Abstract base class for all the user channel.
    """
    @abstractmethod
    def send(self, title: str, message: str) -> None:
        pass
