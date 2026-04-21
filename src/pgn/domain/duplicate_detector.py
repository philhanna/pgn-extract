class DuplicateDetector:
    """
    Port of hashing.c.
    Handles game duplication detection using Zobrist hashes.
    """
    def __init__(self):
        self.seen_hashes = {}

    def is_duplicate(self, game_final_hash: int, cumulative_hash: int) -> bool:
        # Logic from previous_occurance()
        key = (game_final_hash, cumulative_hash)
        if key in self.seen_hashes:
            return True
        self.seen_hashes[key] = True
        return False