from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List, Optional, Dict

class Colour(Enum):
    BLACK = 0
    WHITE = 1

class PieceType(Enum):
    EMPTY = 0
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

@dataclass(frozen=True)
class Piece:
    type: PieceType
    colour: Colour

@dataclass
class Move:
    san: str
    from_square: str  # e.g., "e2"
    to_square: str    # e.g., "e4"
    piece: Piece
    captured: Optional[Piece] = None
    is_check: bool = False
    is_checkmate: bool = False
    nags: List[int] = field(default_factory=list)
    comment: str = ""

@dataclass
class Game:
    tags: Dict[str, str]
    moves: List[Move] = field(default_factory=list)
    final_hash: int = 0
    cumulative_hash: int = 0

class Board:
    def __init__(self):
        # Equivalent to the 12x12 hedge-protected board in C
        self.grid: List[List[Optional[Piece]]] = [[None for _ in range(8)] for _ in range(8)]
        self.to_move = Colour.WHITE
        self.move_number = 1
        self.halfmove_clock = 0
        self.castling_rights = {"K": True, "Q": True, "k": True, "q": True}
        self.en_passant_sq: Optional[str] = None
        self.zobrist_hash: int = 0

    def get_piece_at(self, square: str) -> Optional[Piece]:
        # Logic to convert "e4" to index and return piece
        pass