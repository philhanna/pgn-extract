import chess.pgn  # Using a library like python-chess for the adapter layer
from ..ports.repository import PGNRepository
from ..domain.models import Game, Move

class FilePGNAdapter(PGNRepository):
    def load_games(self, file_path: str):
        with open(file_path) as pgn_file:
            while True:
                pgn_game = chess.pgn.read_game(pgn_file)
                if pgn_game is None:
                    break
                # Map the library object to our Domain Game object
                yield Game(tags=pgn_game.headers)

class ConsoleLoggerAdapter:
    def log(self, message: str):
        # Logic from verbosity handling in argsfile.c
        print(f"[LOG]: {message}")