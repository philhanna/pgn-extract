from dataclasses import dataclass, field
from typing import List, Dict
from .move import Move

@dataclass
class Game:
    tags: Dict[str, str]
    moves: List[Move] = field(default_factory=list)
    final_hash: int = 0
    cumulative_hash: int = 0