from typing import List, Optional
from .colour import Colour
from .piece import Piece

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