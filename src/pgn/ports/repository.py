from abc import ABC, abstractmethod
from typing import Iterable
from ..domain.models import Game

class PGNRepository(ABC):
    @abstractmethod
    def load_games(self, source: str) -> Iterable[Game]:
        pass

class GameOutputPort(ABC):
    @abstractmethod
    def save_game(self, game: Game):
        pass