from pgn.ports.pgn_repository import PGNRepository
from pgn.domain.chess_engine import ChessEngine
from pgn.domain.duplicate_detector import DuplicateDetector

class PGNProcessor:
    def __init__(self, repo: PGNRepository, engine: ChessEngine, detector: DuplicateDetector):
        self.repo = repo
        self.engine = engine
        self.detector = detector

    def process_extraction(self, source: str):
        for game in self.repo.load_games(source):
            if not self.detector.is_duplicate(game.final_hash, game.cumulative_hash):
                # Handle output logic via ports would go here
                pass