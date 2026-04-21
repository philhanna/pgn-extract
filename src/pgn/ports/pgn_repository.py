from abc import ABC, abstractmethod
from typing import Iterable
from pgn.domain.game import Game

class PGNRepository(ABC):
    @abstractmethod
    def load_games(self, source: str) -> Iterable[Game]:
        pass