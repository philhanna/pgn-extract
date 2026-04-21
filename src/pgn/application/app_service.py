from ports.repository import PGNRepository
from domain.chess_engine import ChessEngine, DuplicateDetector

class PGNProcessor:
    def __init__(self, repo: PGNRepository, engine: ChessEngine, detector: DuplicateDetector):
        self.repo = repo
        self.engine = engine
        self.detector = detector

    def process_extraction(self, source: str):
        for game in self.repo.load_games(source):
            # Process moves and check criteria
            # (Equivalent to apply_move_list in apply.c)
            if not self.detector.is_duplicate(game.final_hash, game.cumulative_hash):
                # Handle output...
                pass