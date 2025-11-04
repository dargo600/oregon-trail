
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class UI(ABC):

    @abstractmethod
    def display(self) -> None:
        pass

    @abstractmethod
    def get_user_input(self) -> int:
        pass

    @abstractmethod
    def handle_death(self) -> None:
        pass
