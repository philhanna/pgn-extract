from dataclasses import dataclass, field
from typing import List, Optional
from .piece import Piece

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