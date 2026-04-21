from abc import ABC, abstractmethod
from pgn.domain.game import Game

class GameOutputPort(ABC):
    @abstractmethod
    def save_game(self, game: Game):
        pass