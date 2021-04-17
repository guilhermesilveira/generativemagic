from generativemagic.deck_operations import interweave
from generativemagic.movement import Movement


class InFaro(Movement):
    """In faro shuffle"""

    def apply(self, sequence):
        half = len(sequence) // 2
        return interweave(sequence[half:], sequence[:half])

    def __repr__(self):
        return f"InFaro()"


class OutFaro(Movement):
    """Out faro shuffle"""

    def apply(self, sequence):
        half = len(sequence) // 2
        return interweave(sequence[:half], sequence[half:])

    def __repr__(self):
        return f"OutFaro()"
