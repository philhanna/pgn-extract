import chess.pgn
from pgn.ports.pgn_repository import PGNRepository
from pgn.domain.game import Game

class FilePGNAdapter(PGNRepository):
    def load_games(self, file_path: str):
        with open(file_path) as pgn_file:
            while True:
                pgn_game = chess.pgn.read_game(pgn_file)
                if pgn_game is None:
                    break
                yield Game(tags=pgn_game.headers)