from dataclasses import dataclass
from .colour import Colour
from .piece_type import PieceType

@dataclass(frozen=True)
class Piece:
    type: PieceType
    colour: Colour